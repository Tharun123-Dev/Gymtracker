const API = "http://127.0.0.1:8000/api/workouts/";
const list = document.getElementById("list");

function load(){
 fetch(API)
 .then(res=>res.json())
 .then(data=>{
   list.innerHTML="";
   data.forEach(w=>{
     list.innerHTML+=`<p>${w.name} - ${w.duration} min - ${w.calories} cal</p>`;
   });
 });
}

document.getElementById("form").addEventListener("submit",e=>{
 e.preventDefault();
 fetch(API,{
   method:"POST",
   headers:{'Content-Type':'application/json'},
   body:JSON.stringify({
     name:name.value,
     duration:duration.value,
     calories:calories.value
   })
 }).then(load);
});

load();
