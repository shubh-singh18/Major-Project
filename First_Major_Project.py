import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a=pd.read_excel("minor_project.xlsx")
print(a)

#  question1
#  Display shape, columns, data types, first 10 rows, summary statistics, missing values, and
#  duplicate Order_ID count. Clean missing or duplicate records if found.

print("========================================================")
print("----------------------Question 1--------------------- ")
print("========================================================")

shape=(a.shape)
print("Shape=",shape)

columns=(a.columns)
print("Columns=",columns.tolist())

print("dtypes=",a.dtypes)

Head=(a.head(10))
print("Head =",Head)

describe=(a. describe())
print("Describe =",describe)


Missing_values=(a.isnull().sum())
print("Missing_values =",Missing_values) 

    
Duplicated =a["Order_ID"].duplicated().sum()
print("Duplicate order_Id =",Duplicated)



#  question2
#  Convert Order_Date to datetime if needed. Create Profit_Margin_Pct = Profit_INR / Net_Sales_INR * 100, handling zero denominators safely. 
#  Create Month_Number to preserve calendar order.

print("========================================================")
print("-------------------------Question2--------------------- ")
print("========================================================")

data_time=a["Order_Date"] = pd.to_datetime(a["Order_Date"])
print("Date_time=",data_time)

profit_margin_pct=(a["Profit_INR"]/a["Net_Sales_INR"])*100
print("Profit_margin_pct=",profit_margin_pct)

a["Month_Number"] = a["Order_Date"].dt.month
print(a["Month_Number"])


#  question3
#  Calculate total Net Sales, total Profit, total Orders, total Units, 
#  average Order Value, average Customer Rating, and Return Rate. Show a neat Pandas summary.

print("========================================================")
print("----------------------Question3--------------------- ")
print("========================================================")


total_net_sales=a["Net_Sales_INR"].sum()
print("Total_net=",total_net_sales)

total_profit=a["Profit_INR"].sum()
print("Total_profit=",total_profit)

total_order=a["Order_ID"].count()
print("Total_order=",total_order)

total_units=a["Units"].sum()
print("Total_units=",total_units)

average_order_values=total_net_sales/total_order
print("Average_order_vaalues =",average_order_values)

average_customer_rating=a["Customer_Rating"].mean()
print("Average_customer_rating=",average_customer_rating)

Total_return=a[a["Returned"]=="Yes"]["Order_ID"].count()
print("Total_return=",Total_return)

Return_Rate=(Total_return)/(total_order)*100
print("Return_Rate=",Return_Rate)





#  question4
#  Group by month and calculate Net_Sales_INR and Profit_INR totals. Plot sales and profit as two lines in one chart or separate subplots.
#  Add title, labels, markers, colors, grid, and legend.

print("========================================================")
print("----------------------Question4--------------------- ")
print("========================================================")

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Net_sale=a.groupby("Month_Number")["Net_Sales_INR"].sum()
print(Net_sale)
Profit_Inr=a.groupby("Month_Number")["Profit_INR"].sum()
plt.figure(figsize=(10,8))
plt.plot(Net_sale.index,Net_sale.values,label="Net Sales",marker="o",color="#F59E0B")
plt.xticks(range(1,13,1),labels=month_names)
plt.text(1,4400000, "4356892")
plt.text(2,4200000,"4128793")
plt.text(3,3200000,"3114912.85")
plt.text(4,4700000," ₹ 4648282")
plt.text(5,2200000," ₹ 2138591")
plt.text(6,4700000," ₹ 4639741")
plt.text(7,3900000," ₹ 3823858")
plt.text(8,4600000," ₹ 4505341")
plt.text(9,2600000," ₹ 2541882")
plt.text(10,4800000," ₹ 4734604")
plt.text(11,3700000," ₹ 3621247")
plt.text(12,5000000," ₹ 4978264")

plt.plot(Profit_Inr.index,Profit_Inr.values,label="Profit Sales",marker="o",color="#7C3AED")
plt.yticks(range(100000,5200000,500000))
plt.text(1 ,1200000 ,"₹ 1160602")
plt.text(2 ,1200000,"₹ 1128130")
plt.text(3,900000,"₹ 858289")
plt.text(4,1300000,"₹ 1236440")
plt.text(5,600000,"₹ 595579")
plt.text(6,1400000,"₹ 1351547")
plt.text(7,1100000,"₹ 1003400")
plt.text(8,1200000,"₹ 1169098")
plt.text(9,700000,"₹ 685203")
plt.text(10,1400000,"₹ 1331549")
plt.text(11,1000000,"₹ 911942")
plt.text(12,1400000,"₹ 1325369")

plt.title("Total Sales vs Total Profit",color="#1E3A8A",fontsize=20)
plt.xlabel("Months",color="#6D28D9",fontsize=17)
plt.ylabel("Net Sales",color="#6D28D9",fontsize=15)
plt.yticks(range(100000,5000000,300000))
plt.ylim(100000,5000001)
plt.ticklabel_format(style="plain",axis="y")
plt.grid()
plt.legend()
plt.savefig("question4.png")  
plt.show()


#  question5
#  Group by Product and calculate total net sales, profit, units sold, and average rating. Sort by net sales descending. 
#  Plot top 8 products in a bar chart. Use plt.text() to show values above bars.


print("========================================================")
print("----------------------Question5--------------------- ")
print("========================================================")
group_by_product=a.groupby("Product").agg({
    "Net_Sales_INR":"sum",
    "Profit_INR":"sum",
    "Units":"sum",
    "Customer_Rating":"mean"
})
print(group_by_product)
top_8=group_by_product.sort_values("Net_Sales_INR",ascending=False).head(8)
print(top_8)
plt.figure(figsize=(10,6))
bars=plt.bar(top_8.index,top_8["Net_Sales_INR"],color="#10B981")
plt.bar_label(bars,fmt="%.0f")
plt.title("Top 8 Best-Selling Products by Net Sales",color="#263238",fontsize=18)
plt.xlabel("Product Names",color="#F97316",fontsize=15)
plt.ylabel("Net Sales (INR)",color="#F97316",fontsize=15)
plt.ticklabel_format(style="plain",axis="y")
plt.savefig("question5.png")
plt.show()

#  question 6
#  Group by City and calculate net sales, profit, order count, and average rating.
#  Sort cities by net sales. Create a horizontal bar chart and set suitable axis limits and ticks
print("========================================================")
print("----------------------Question6--------------------- ")
print("========================================================")

Group_by_Net_Sales_INR=a.groupby("City")["Net_Sales_INR"].sum()
print(Group_by_Net_Sales_INR)

Group_by_Profit_INR=a.groupby("City")["Profit_INR"].sum()
print(Group_by_Profit_INR)
Group_by_Order=a.groupby("City")["Order_ID"].count()
print(Group_by_Order)
Group_by_Customer_Rating=a.groupby("City")["Customer_Rating"].mean()
print(Group_by_Customer_Rating)

Sort_cities_by_net_sales=Group_by_Net_Sales_INR.sort_values(ascending=False)
print(Sort_cities_by_net_sales)
plt.figure(figsize=(10,8))
bar=plt.barh(Sort_cities_by_net_sales.index,Sort_cities_by_net_sales.values,color="#008C95")
plt.bar_label(bar,fmt="%.0f")
plt.xlim(0,7000000)
plt.xticks(range(100000,7000000,1000000))
plt.xlabel("Net_Sales_INR",color="#263238",fontsize=15)
plt.ylabel("City",color="#263238",fontsize=15)
plt.title("City-wise Net Sales Analysis",color="#263238",fontsize=20)
plt.ticklabel_format(style="plain",axis="x")
plt.savefig("question6.png")
plt.show()


#  question 7
#  Calculate each Category's share of total Net Sales. Create a pie chart with labels, autopct='%1.1f%%', distinct colors, and startangle=90.
#   Change individual category label colors using the texts returned by plt.pie().
print("========================================================")
print("----------------------Question 7--------------------- ")
print("========================================================")

Calculate_category_share=a.groupby("Category")["Net_Sales_INR"].sum()
print(Calculate_category_share)
var=["#0F766E", "#F59E0B", "#7C3AED"]
plt.pie(Calculate_category_share.values,labels=Calculate_category_share.index,autopct="%1.1f%%",colors=var,startangle=90)
plt.title("Category-wise Net Sales Contribution",fontsize=18,color= "#1E293B")
plt.savefig("question7.png")
plt.show()



#  question 8

#  Compare total net sales and order counts across Sales_Channel. Identify the best channel using Pandas. 
#  Plot a bar chart with title, labels, colors, grid, and legend.
print("========================================================")
print("----------------------Question 8--------------------- ")
print("========================================================")

compare_sales_channel=a.groupby("Sales_Channel")["Order_ID"].count()
print(compare_sales_channel)
comapre_net_sales=a.groupby("Sales_Channel")["Net_Sales_INR"].sum()
print(comapre_net_sales)

print(compare_sales_channel.idxmax())
print(comapre_net_sales.idxmax())
plt.figure(figsize=(15,8))
plt.subplot(1,2,1)
barss=plt.bar(compare_sales_channel.index,compare_sales_channel.values,label="Order Count",color="#3B82F6")
plt.bar_label(barss)
plt.title("Order Count by Sales Channel",color="#1E293B",fontsize=20)
plt.xlabel("Sales Channel",color="#F97316",fontsize=15)
plt.ylabel("Number of Orders",color="#F97316",fontsize=15)
plt.legend()
plt.grid(axis="y")

plt.subplot(1,2,2)
bar=plt.bar(comapre_net_sales.index,comapre_net_sales.values,label="Net Sales",color="#10B981")
plt.bar_label(bar,fmt="%.0f")
plt.title("Net Sales by Sales Channel",color="#1E293B", fontsize=17,)
plt.xlabel("Sales Channel", color="#F97316",fontsize=15)
plt.ylabel("Net Sales (INR)", color="#F97316",fontsize=15)
plt.ticklabel_format(style="plain", axis="y")
plt.suptitle("Compare Total Net Sales and  Sales_Channel",color="#F50808",fontsize=20)
plt.tight_layout()
plt.savefig("question8.png")
plt.show()


# question 9
#  Calculate rating counts and average rating by Product and by City.
#  Create a histogram of Customer_Rating using bins=5. Explain the overall rating distribution.
print("========================================================")
print("----------------------Question 9----------------------- ")
print("========================================================")



calculate_rating_count_product=a.groupby("Product")["Customer_Rating"].count()
print(calculate_rating_count_product)

calculate_rating_average_product=a.groupby("Product")["Customer_Rating"].mean()
print(calculate_rating_average_product)

calculate_rating_count_city=a.groupby("City")["Customer_Rating"].count()
print(calculate_rating_count_city)


calculate_rating_average_city=a.groupby("City")["Customer_Rating"].mean()
print(calculate_rating_average_city)


plt.hist(a["Customer_Rating"],color="#14B8A6")
plt.title("Customer Rating Distribution",color="#1E3A8A",fontsize=18)
plt.xlabel("Customer_Rating",color="#1E3A8A",fontsize=15)
plt.ylabel("frequency",color="#1E3A8A",fontsize=15)
plt.grid(axis="y")
plt.text(1.2,63,"63",color="red")
plt.text(2,103,"103",color="red")
plt.text(3.1,273,"273",color="red")
plt.text(3.9,537,"537",color="red")
plt.text(4.7,524,"524",color="red")
plt.savefig("question9.png")
plt.show()






#  Expalin the overall rating distribution
#  Most customers ne 3.5 se 4.0 ke beech rating di hai, iska matlab customers mostly satisfied hain.
#  1 se 1.5 ke beech sabse kam customers ne rating di hai.



#  question 10
#  Group by Discount_Rate and calculate total net sales, total profit, and average profit margin.
#  Identify the discount level with the highest total profit. Present findings using a bar chart.

print("========================================================")
print("----------------------Question 10--------------------- ")
print("========================================================")



Calculate_total_net_sales=a.groupby("Discount_Rate")["Net_Sales_INR"].sum()
print(Calculate_total_net_sales)
calculate_total_profit=a.groupby("Discount_Rate")["Profit_INR"].sum()
print(calculate_total_profit)


a["Profit_margin"]=a["Profit_INR"]/a["Net_Sales_INR"]*100
calculate_average_profit_margin=a.groupby("Discount_Rate")["Profit_margin"].mean()
print(calculate_average_profit_margin)


print(calculate_total_profit.idxmax())
plt.figure(figsize=(10,8))
bars=plt.bar(calculate_total_profit.index,calculate_total_profit.values,color="#14B8A6",label="total profits",width=0.03)
plt.bar_label(bars, fmt="%.0f", padding=3)
plt.title("Discount Rate and Total Profit Rate",color="brown",fontsize=20)
plt.xlabel("Discount Rate",color="brown",fontsize=15)
plt.ylabel("Total Profit Rate",color="brown",fontsize="15")
plt.yticks(range(0, 4000001, 500000))
plt.ticklabel_format(style="plain",axis="y")
plt.grid(axis="y")
plt.savefig("question10.png")
plt.show()



#  question 11
#  Compare returned vs non-returned orders. Calculate order counts and net sales by Returned status. 
#  Calculate return rate by Product and identify products with the highest return rates.

print("========================================================")
print("----------------------Question 11--------------------- ")
print("========================================================")



compare_returned=a.groupby("Returned")["Order_ID"].count()
print("Compare_returned = ",compare_returned)

calculate_returned_sales=a.groupby("Returned")["Net_Sales_INR"].sum()
print("Calculate_returned_sales = ",calculate_returned_sales)

a["Return_Flag"] = a["Returned"].map({"Yes": 1, "No": 0})
Calculate_return_rate=a.groupby("Product")["Return_Flag"].mean() * 100
print("Calculate__return_rate = ",Calculate_return_rate)
print(Calculate_return_rate.idxmax())

compare_product_return = a.groupby(["Product", "Returned"])["Order_ID"].count().unstack(fill_value=0)
print(compare_product_return)
plt.figure(figsize=(10,8))
bars = compare_product_return.plot(
    kind="bar",
    color=["#14B8A6", "#F59E0B"]
)
plt.title("Product-wise Returned vs Non-Returned Orders",color="#1E3A8A",fontsize=20)
plt.xlabel("Product",color="#F97316",fontsize=15)
plt.ylabel("Total Orders",color="#F97316",fontsize=15)
plt.xticks(rotation=45)
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.text(-0.2, 153, "152",color="red")
plt.text(0.1, 11, "9",color="red")

plt.text(0.8, 129, "127",color="red")
plt.text(1.1, 8, "6",color="red")

plt.text(1.8, 129, "128",color="red")
plt.text(2.1, 15, "13",color="red")

plt.text(2.8, 166, "164",color="red")
plt.text(3.1, 10, "9",color="red")

plt.text(3.8, 138, "136",color="red")
plt.text(4.1, 13, "11",color="red")

plt.text(4.8, 134, "132",color="red")
plt.text(5.1, 15, "13",color="red")

plt.text(5.8, 139, "137",color="red")
plt.text(6.1, 10, "8",color="red")

plt.text(6.8, 147, "145",color="red")
plt.text(7.1, 10, "8",color="red")

plt.text(7.8, 150, "148",color="red")
plt.text(8.1, 16, "14",color="red")

plt.text(8.8, 127, "126",color="red")
plt.text(9.1, 16, "14",color="red")
plt.savefig("question11.png")
plt.show()


# question 12
# Calculate average Shipping_Days by City and Sales_Channel. Identify the slowest city and channel. 
#  Create a bar chart of average shipping days by city.



print("========================================================")
print("----------------------Question 12--------------------- ")
print("========================================================")


calculate_average_shipping_city=a.groupby("City")["Shipping_Days"].mean()
print(calculate_average_shipping_city)
print(calculate_average_shipping_city.idxmax())

calculate_average_shipping_sales_channel=a.groupby("Sales_Channel")["Shipping_Days"].mean()
print(calculate_average_shipping_sales_channel)
print(calculate_average_shipping_sales_channel.idxmax())

plt.figure(figsize=(10,8))
bars=plt.bar(calculate_average_shipping_city.index,calculate_average_shipping_city.values,color="#14B8A6")
plt.bar_label(bars)

plt.xlabel("City",color="darkgreen",fontsize=14)
plt.ylabel("Average Shipping Days",color="darkgreen",fontsize=14)
plt.title("Average Shipping Days by City",color="darkgreen",fontsize=18)
plt.savefig("question12.png")
plt.show()

# question13
# Create a scatter plot with Units on X-axis and Net_Sales_INR on Y-axis. Discuss the relationship. 
# Calculate a Pandas correlation matrix for Units, Unit_Price_INR, Net_Sales_INR, Profit_INR, Customer_Rating, and Shipping_Days.

print("========================================================")
print("----------------------Question 13--------------------- ")
print("========================================================")



group_units=a.groupby("Units")["Net_Sales_INR"].sum()
print(group_units)


plt.figure(figsize=(10,8))
plt.scatter(group_units.index,group_units.values,color="#0F766E")
plt.title("Units vs Net Sales",color="#6D28D9",fontsize=28)
plt.xlabel("Units",color="#6D28D9",fontsize=15)
plt.ylabel("Net Sales (INR)",color="#6D28D9",fontsize=15)
plt.ticklabel_format(style="plain",axis="y")
plt.text(1,13712156,"13712156",color="red")
plt.text(2,12775334,"12775334",color="red")
plt.text(3,10018790,"10018791",color="red")
plt.text(4,6663221,"6663222",color="red")
plt.text(5,4062908,"4062909",color="red")
plt.grid()
plt.savefig("question13.png")
plt.show()





#  question 14
# Create one figure with 4 subplots (2 rows × 2 columns): (1) monthly net sales line plot, (2) top 8 products bar chart, 
#  (3) customer rating histogram, (4) category revenue-share pie chart.
#  Give each subplot a title and suitable labels. Use figsize, plt.tight_layout(), and save as retail_dashboard.png with dpi=300.



print("========================================================")
print("----------------------Question 14---------------------- ")
print("========================================================")

plt.figure(figsize=(15,8))
plt.subplot(2,2,1)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Net_sale=a.groupby("Month_Number")["Net_Sales_INR"].sum()
print(Net_sale)
Profit_Inr=a.groupby("Month_Number")["Profit_INR"].sum()

plt.plot(Net_sale.index,Net_sale.values,label="Net Sales",marker="o",color="#F59E0B")
plt.xticks(range(1,13,1),labels=month_names)
plt.text(1,4400000, "4356892")
plt.text(2,4200000,"4128793")
plt.text(3,3200000,"3114912.85")
plt.text(4,4700000," ₹ 4648282")
plt.text(5,2200000," ₹ 2138591")
plt.text(6,4700000," ₹ 4639741")
plt.text(7,3900000," ₹ 3823858")
plt.text(8,4600000," ₹ 4505341")
plt.text(9,2600000," ₹ 2541882")
plt.text(10,4800000," ₹ 4734604")
plt.text(11,3700000," ₹ 3621247")
plt.text(12,5000000," ₹ 4978264")
plt.plot(Profit_Inr.index,Profit_Inr.values,label="Profit Sales",marker="o",color="#7C3AED")
plt.yticks(range(100000,5200000,500000))
plt.text(1 ,1200000 ,"₹ 1160602")
plt.text(2 ,1200000,"₹ 1128130")
plt.text(3,900000,"₹ 858289")
plt.text(4,1300000,"₹ 1236440")
plt.text(5,600000,"₹ 595579")
plt.text(6,1400000,"₹ 1351547")
plt.text(7,1100000,"₹ 1003400")
plt.text(8,1200000,"₹ 1169098")
plt.text(9,700000,"₹ 685203")
plt.text(10,1400000,"₹ 1331549")
plt.text(11,1000000,"₹ 911942")
plt.text(12,1400000,"₹ 1325369")

plt.title("Total Sales vs Total Profit",color="#1E3A8A")
plt.xlabel("Months",color="#6D28D9")
plt.ylabel("",color="#6D28D9")
plt.yticks(range(100000,5000000,300000))
plt.ylim(100000,5000001)
plt.ticklabel_format(style="plain",axis="y")
plt.grid()
plt.legend()


plt.subplot(2,2,2)
group_by_product=a.groupby("Product").agg({
    "Net_Sales_INR":"sum",
    "Profit_INR":"sum",
    "Units":"sum",
    "Customer_Rating":"mean"
})
print(group_by_product)
top_8=group_by_product.sort_values("Net_Sales_INR",ascending=False).head(8)
print(top_8)
bars=plt.bar(top_8.index,top_8["Net_Sales_INR"],color="#10B981")
plt.bar_label(bars,fmt="%.0f")
plt.title("Top 8 Best-Selling Products by Net Sales",color="#263238")
plt.xlabel("Product Names",color="#F97316",rotation=45)
plt.ylabel("Net Sales (INR)",color="#F97316")
plt.ticklabel_format(style="plain",axis="y")

plt.subplot(2,2,3)

calculate_rating_count_product=a.groupby("Product")["Customer_Rating"].count()
print(calculate_rating_count_product)

calculate_rating_average_product=a.groupby("Product")["Customer_Rating"].mean()    
print(calculate_rating_average_product)

calculate_rating_count_city=a.groupby("City")["Customer_Rating"].count()
print(calculate_rating_count_city)


calculate_rating_average_city=a.groupby("City")["Customer_Rating"].mean()
print(calculate_rating_average_city)



plt.hist(a["Customer_Rating"],color="#14B8A6")
plt.title("Customer Rating Distribution",color="#1E3A8A",fontsize=18)
plt.xlabel("Customer_Rating",color="#1E3A8A",fontsize=15)
plt.ylabel("frequency",color="#1E3A8A",fontsize=15)
plt.grid(axis="y")
plt.text(1.2,63,"63",color="red")
plt.text(2,103,"103",color="red")
plt.text(3.1,273,"273",color="red")
plt.text(3.9,537,"537",color="red")
plt.text(4.7,524,"524",color="red")




plt.subplot(2,2,4)
Calculate_category_share=a.groupby("Category")["Net_Sales_INR"].sum()
print(Calculate_category_share)
var=["#0F766E", "#F59E0B", "#7C3AED"]
plt.pie(Calculate_category_share.values,labels=Calculate_category_share.index,autopct="%1.1f%%",colors=var,startangle=90)
plt.title("Category-wise Net Sales Contribution",color= "#1E293B")
plt.suptitle("Retail Sales Dashboard ",color="red",fontsize=20)
plt.tight_layout()
plt.savefig("retail_dashboard.png")

plt.show()

    

#  question 15

#  Write 5 evidence-based findings, including best product, best city, best sales channel,
#  return-rate concern, and one recommendation to improve sales or customer satisfaction.

# print("========================================================")
# print("----------------------Question 15--------------------- ")
# print("========================================================")
#  Best Product=Laptop : laptop ki sales sabse zyada hai isne 15733407(one crore fifty seven lakh thiry three thousand four hundred seven),ki net sales
#  aur 4022349(Forty lakh twenty-two thousand three hundred forty-nine)ka profit generate kiya hai

#  Best city : Mumbai:Mumbai mein sabse zyada sales hui hain.Mumbai ki total net sales
#   6583396(Sixty-Five Lakh Eighty-Three Thousand Three Hundred Ninety-Six.)

#  Best sales channel : WEBSIte :website se sabse zyaba net sales gernrate hui hain,jo 
#  13206859(One Crore Thirty-Two Lakh Six Thousand Eight Hundred Fifty-Nine.) hain

#  Return rate concern : Tablet:Tablet ka return rate sabse zyada 10% hai.overall 1500 recors main se 
# 105 records return hue hain ,yani overall retrun rate 7% hai 

#  Recommendation:Tablet ke return kam karne ke liye product quality check kaarni chahiye,
#  delivery ke time damage check karna chahiye aur product ki details sahi deni chahiye.isse customer satisfaction improve ho sakit hai
