"use strict";
const searchIcon = document.querySelector(".search__icon");
const searchBox = document.querySelector(".search__input");
const Category = document.querySelector(".category");
const dropMenu = document.querySelector(".drop--link");
const slides = document.querySelectorAll(".person");
const btnLeft = document.querySelector(".slider__btn--left");
const btnRight = document.querySelector(".slider__btn--right");
const message = document.querySelector(".message");
const productList = document.querySelector(".products_list");
const productRow = document.querySelector(".product__row");
const product = document.querySelector(".row");
const categoryLink=document.querySelector(".product__link");
const reviewButton=document.querySelector(".reviewbutton");
const modal=document.querySelector(".modal");
const overlay=document.querySelector(".overlay");
const closeModal=document.querySelector(".exit");
const custName=document.querySelector(".rn");
const custimg=document.querySelector(".review_img");
const inputReview=document.querySelector(".review_input");
const submitReview=document.querySelector(".review_submit")
const fmsg=document.querySelector(".farmermessage");
const fname=document.querySelector(".farmername");
const fimg=document.querySelector(".farmaimage");
//***************Search bos**************
let count = 1;
searchIcon.addEventListener("click", function () {
  if (count == 1) {
    searchBox.style.display = "block";
    count = 0;
  } else {
    count = 1;
    searchBox.style.display = "none";
  }
});

//*********************************slider********************//

const maxSlide = slides.length;
// message.style.translate = "scale(0.2)";
// message.style.overflow = "visible";


const goToSlide = function (slide) {
  slides.forEach(
    (s, i) => (s.style.transform = `translateX(${100 * (i - slide)}%)`)
  );
};
goToSlide(0);
const nextSlide = function () {
  if (currSlide === maxSlide - 1) currSlide = 0;
  else currSlide++;
  goToSlide(currSlide);
};
const prevSlide = function () {
  if (currSlide === 0) currSlide = maxSlide - 1;
  else currSlide--;
  goToSlide(currSlide);
};
//btnLeft.addEventListener("click", prevSlide);
//btnRight.addEventListener("click", nextSlide);

//*************Showing products on site*****************//

let p=0;

let obj1;
let obj2;
let obj3;
productList.innerHTML = "";
for(;p<Object.keys(data).length;){
obj1=data[p];
++p;
obj2=data[p];
++p;
obj3=data[p];
++p;

const html = `<div class="product__row" enctype="multipart/form-data">
<div class="row">
  <div class="image" enctype="multipart/form-data">
    <img src="/${obj1['image']}"  alt="product" />
    <button class="buy">Buy Now +</button>
    <button class="add_to_cart">Add to cart 🛒</button>
  </div>
  <div class="products__detail">
    <p class="company">${obj1['company']}</p>
    <span class="type">${obj1['category']}</span>
    <p class="name">${obj1['Name']}</p>
    <span class="fakeprice"><strike>900$</strike></span>
    <span class="price">${obj1['price']}</span>
  </div>
</div>
<div class="row">
  <div class="image">
    <img src="/${obj2['image']}" alt="product" />
    <button class="buy">Buy Now +</button>
    <button class="add_to_cart">Add to cart 🛒</button>
  </div>
  <div class="products__detail">
    <p class="company">${obj2['company']}</p>
    <span class="type">${obj2['category']}</span>
    <p class="name">${obj2['Name']}</p>
    <span class="fakeprice"><strike>1000$</strike></span>
    <span class="price">${obj2['price']}</span>
  </div>
</div>
<div class="row">
  <div class="image">
    <img src="/${obj3['image']}" alt="product" />
    <button class="buy">Buy Now +</button>
    <button class="add_to_cart">Add to cart 🛒</button>
  </div>
  <div class="products__detail">
    <p class="company">${obj3['company']}</p>
    <span class="type">${obj3['category']}</span>
    <p class="name">${obj3['Name']}</p>
    <span class="fakeprice"><strike>500$</strike></span>
    <span class="price">${obj3['price']}</span>
  </div>
</div>
</div>`;


productList.insertAdjacentHTML("afterbegin", html);
}

//******************review-modal*********************

reviewButton.addEventListener("click",function(e){
if(user_data.name!=undefined){
e.preventDefault();
modal.classList.remove('hidden');
overlay.classList.remove('hidden');
custName.innerHTML=user_data.name;
custimg.src=`/${user_data.image}`;
}
else alert('You are not logged to your account');
});


const close=function(){
modal.classList.add('hidden');
overlay.classList.add('hidden');
};
closeModal.addEventListener("click",close);
overlay.addEventListener("click",close);

function passdata(){
const input=inputReview.value;
console.log(input)
inputReview.value=" ";
close();
$.ajax({
url:'review/',
data:{
'userInput':input,
},
success:function(){
alert(`Thankyou for your feedback ${user_data.name}`);
window.location.reload();
}
})
};

//********************slider**********************//
let currSlide = 0;
const arr=[]
const dLen=Object.keys(d).length;
fmsg.innerHTML=d[currSlide].review;
fname.innerHTML=d[currSlide].name;
fimg.src=`/${d[currSlide].image}`;

btnRight.addEventListener("click",function(e){
e.preventDefault()
if(currSlide!=dLen-1) {
arr.push(currSlide);
currSlide++;
fmsg.innerHTML=d[currSlide].review;
fname.innerHTML=d[currSlide].name;
fimg.src=`/${d[currSlide].image}`;
}
})

btnLeft.addEventListener("click",function(e){
e.preventDefault()
if(currSlide!=0){
if(arr[arr.length-1]==dLen) arr.pop();
let num=arr.pop();
fmsg.innerHTML=d[num].review;
fname.innerHTML=d[num].name;
fimg.src=`/${d[num].image}`;
currSlide--;
}
})