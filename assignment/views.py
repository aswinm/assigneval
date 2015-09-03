from django.shortcuts import render
from assignment.models import Assignment,Submission
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from assignment.forms import AssignmentForm,SubForm
from django.contrib.auth.decorators import login_required
from cosine import check_plagiarism
from wordcompare import compare_words
from lda import sentence_comparison

import datetime
from django.utils import timezone


def get_grade(score):
    if score>90:
        return "S"
    elif score > 80:
        return "A"
    elif score > 70:
        return "B"
    elif score > 60:
        return "C"
    elif score > 55:
        return "D"
    elif score > 50:
        return "E"
    else:
        return "U"

@staff_member_required
def assignments(request):
    a = Assignment.objects.filter(user=request.user)
    return render(request,"assignments.html",{'assignments':a})

@staff_member_required
def assignment(request,aid):
    a = Assignment.objects.filter(aid=aid).first()
    s = Submission.objects.filter(assignment = a)
    p = s.filter(is_plagiarism = True)
    s = s.filter(is_plagiarism = False)
    if not a:
        return HttpResponseRedirect("/assignments")
    return render(request,"assignment.html",{'assignment':a,'plagiarisms':p,'assignments':s})

@staff_member_required
def addassignment(request,aid = None):
    d = {}
    d["url"] = "/assignments/add"
    d["sub"] = "Add"
    if aid:
        a = Assignment.objects.filter(aid=aid).first()
        if not a:
            return HttpResponseRedirect("/assignments")
    else:
        a = None
    if request.method == "POST":
        form = AssignmentForm(request.POST,request.FILES,instance=a) 
        if form.is_valid():
            a = form.save(commit = False)
            a.user = request.user
            a.sample_copy = form.cleaned_data["sample_copy"]
            a.save()
            return HttpResponseRedirect("/assignments")
        else:
            d["form"] = form
            d["text"] = form.errors
            print form.errors
            return render(request,"register.html",d)
    else:
        d["form"] = AssignmentForm(instance=a)
        return render(request,"register.html",d)

@staff_member_required
def deleteassignment(request,aid):
    a = Assignment.objects.filter(aid=aid).first()
    if a:
        a.delete()
    return HttpResponseRedirect("/assignments")

@login_required
def submit(request):
    d = {}
    d["url"] = "/submit"
    d["sub"] = "Submit"
    if request.method == "POST":
        form = SubForm(request.POST,request.FILES)
        if form.is_valid():

            a = form.cleaned_data["assignment"]
            if a.deadline < timezone.now():
                return render(request,"register.html",{'text':"The Assignment deadline is up!!!"})
            
            s = Submission.objects.filter(assignment=a,user=request.user,is_plagiarism = False).first()
            if s:
                return render(request,"register.html",{'text':'You have already submitted this assignment'})


            s = form.save(commit = False)
            s.user = request.user
            s.submitted_at = datetime.datetime.now()
            s.answer = form.cleaned_data["answer"]
            
            submissions = Submission.objects.filter(assignment = s.assignment)
            answer = s.answer.read().lower()
            
            for submission in submissions:
                sub = submission.answer.read().lower()
                print "Sub: "+ sub
                if check_plagiarism(answer,sub):
                    s.is_plagiarism = True
                    s.save()
                    d["form"] = SubForm()
                    d["text"] = "Plagiarism Found. The incident will be reported"

                    return render(request,"register.html",d)
            sample_answer = s.assignment.sample_copy.read().lower()
    
            w_c = compare_words(sample_answer,answer) 
            s_c = sentence_comparison(sample_answer,answer)
            print w_c,s_c
            s.score = (float((w_c))+s_c)/2
            s.grade = get_grade(s.score*100)
            s.save()
            d["form"] = SubForm()
            d["text"] = "Submission Successful"
            return render(request,"register.html",d)
        else:
            d["form"] = form
            return render(request,"register.html",d)

    else:
        d["form"] = SubForm()
        return render(request,"register.html",d)




# Create your views here.
