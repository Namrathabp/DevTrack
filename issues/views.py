from django.shortcuts import render
import json, os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reporter, Issue, CriticalIssue, LowPriorityIssue

REPORTERS_FILE = 'reporters.json'
ISSUES_FILE = 'issues.json'

def init_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump([], f)

@csrf_exempt
def manage_reporters(request):
    init_file(REPORTERS_FILE)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            reporter = Reporter(data['id'], data['name'], data['email'], data['team'])
            reporter.validate()
            
            with open(REPORTERS_FILE, 'r+') as f:
                reporters = json.load(f)
                reporters.append(reporter.to_dict())
                f.seek(0)
                json.dump(reporters, f)
            return JsonResponse(reporter.to_dict(), status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    elif request.method == 'GET':
        rep_id = request.GET.get('id')
        with open(REPORTERS_FILE, 'r') as f:
            reporters = json.load(f)
        
        if rep_id:
            reporter = next((r for r in reporters if r['id'] == int(rep_id)), None)
            return JsonResponse(reporter, status=200) if reporter else JsonResponse({'error': 'Not found'}, status=404)
        return JsonResponse(reporters, safe=False)

@csrf_exempt
def manage_issues(request):
    init_file(ISSUES_FILE)

    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            # Polymorphic instantiation based on priority
            p = data.get('priority')
            params = (data['id'], data['title'], data['description'], data['status'], p, data['reporter_id'])
            
            if p == 'critical':
                issue = CriticalIssue(*params)
            elif p == 'low':
                issue = LowPriorityIssue(*params)
            else:
                issue = Issue(*params)

            issue.validate()
            res_data = issue.to_dict()
            res_data['message'] = issue.describe()

            with open(ISSUES_FILE, 'r+') as f:
                issues = json.load(f)
                issues.append(res_data)
                f.seek(0)
                json.dump(issues, f)
            return JsonResponse(res_data, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    elif request.method == 'GET':
        issue_id = request.GET.get('id')
        status_filter = request.GET.get('status')
        with open(ISSUES_FILE, 'r') as f:
            issues = json.load(f)

        if issue_id:
            issue = next((i for i in issues if i['id'] == int(issue_id)), None)
            return JsonResponse(issue, status=200) if issue else JsonResponse({'error': 'Issue not found'}, status=404)
        
        if status_filter:
            issues = [i for i in issues if i['status'] == status_filter]
            
        return JsonResponse(issues, safe=False)

# Create your views here.
