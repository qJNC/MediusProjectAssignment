from django.shortcuts import render
from upload.models import uploader,files
from django.db import models

def home(request):
    if request.method=="POST":
        file=request.POST.get("Folder")
        name=request.POST.get("name")
        About=request.POST.get("about")

        obj=uploader.objects.create(Name=name,About=About,File=file)
        obj.save()
    return render(request,"home.html")
    
def summary(request):
    q=files.objects.values("CustPin").distinct()
    s=q.count()
    summary_data = files.objects.values('CustState', 'DPD',"CustPin","ACCNO").annotate(count=models.Count('id'))
    mp_no = q.filter(CustState='MADHYA PRADESH').count()
    mp_no = int(mp_no)
    as_no = q.filter(CustState='ASSAM').count()
    as_no = int(as_no)
    hr_no = q.filter(CustState='HARYANA').count()
    hr_no = int(hr_no)
    dl_no = q.filter(CustState='DELHI').count()
    dl_no = int(dl_no)
    mh_no = q.filter(CustState='MAHARASHTRA').count()
    mh_no = int(mh_no)
    wb_no = q.filter(CustState='WEST BENGAL').count()
    wb_no = int(wb_no)
    od_no = q.filter(CustState='ODISHA').count()
    od_no = int(od_no)
    tn_no = q.filter(CustState='TAMIL NADU').count()
    tn_no = int(tn_no)
    state_list = ["MADHYA PRADESH","ASSAM","HARYANA","DELHI","MAHARASHTRA","WEST BENGAL","ODISHA","TAMIL NADU"]
    numb_list = [mp_no,as_no,hr_no,dl_no,mh_no,wb_no,od_no,tn_no]
    context={
        "data":summary_data,
        "states":state_list,
        "numbers":numb_list,
        "total":s,
    }
    return render(request,"summary.html",context)

