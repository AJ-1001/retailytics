from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Sale

#  Main Dashboard
def main_page(request):
    return render(request, "sales/main_page.html", {
        "logo_path": "/static/images/logo.jpg"
    })

#  Add Sale Data
def sales_add(request):
    if request.method == "POST":
        Sale.objects.create(
            date=request.POST["date"],
            store_name=request.POST["store_name"],
            location=request.POST["location"],
            product_name=request.POST["product_name"],
            category=request.POST["category"],
            units_sold=request.POST["units_sold"],
            selling_price=request.POST["selling_price"],
            discount=request.POST["discount"],
            total_revenue=float(request.POST["selling_price"]) * (1 - float(request.POST["discount"])) * int(request.POST["units_sold"])
        )
        return redirect("sales_html")
    return render(request, "sales/sales_add.html",{"logo_path": "/static/images/logo.jpg"})

#  Calculate Metrics
def sales_top(request):
    total_revenue = Sale.objects.aggregate(Sum("total_revenue"))["total_revenue__sum"] or 0
    top_products = Sale.objects.values("product_name").annotate(total=Sum("total_revenue")).order_by("-total")[:5]
    return render(request, "sales/sales_top.html", {"total_revenue": total_revenue, "top_products": top_products, "logo_path": "/static/images/logo.jpg"})

#  Sales Table with Search/Filter
def sales_list(request):
    query = request.GET.get("q")
    filter_by = request.GET.get("filter_by")

    sales = Sale.objects.all()

    if query and filter_by:
        if filter_by == "date":
            sales = sales.filter(date=query)
        elif filter_by == "category":
            sales = sales.filter(category__icontains=query)
        elif filter_by == "store":
            sales = sales.filter(store__icontains=query)
        elif filter_by == "product_name":
            sales = sales.filter(product_name__icontains=query)
        else:
            sales = sales  

    return render(request, "sales/sales_list.html", {"sales": sales, "query": query, "filter_by": filter_by, "logo_path": "/static/images/logo.jpg"})
