var mydict = {
    0:["Magharetta Regular",199],
    1:["Non-Veg Medium",250],
    2:["Cheese N Corn- 169 Rs",169],
    3:["Double Cheese Mag",199],
    4:["Indi Tandoori ",249],
    5:["Non-Veg Supreme",319],
    6:["Hakka Noodle",100],
    7:["Coke",75],
    8:["Veg Momo",60],
    9:["Veg Fried Momo",70],
    10:["tandori Chicken 2 leg piece",170],
    11:["Ice cream",100]
}
var total = 0;
var item = ""
function calculateprice(){
var foods = document.getElementsByName('Pizza[]'); 
for(let i=0 ;i < foods.length;i++){
    if(foods[i].checked == true){
        total += mydict[i][1];
        item += mydict[i][0] +" "
    }
}
document.getElementById("total").innerHTML = "You have Ordered Food of " + total +"  Rupees"

document.getElementById("items_ordered").innerHTML = "You Orders are :  " + item
}



