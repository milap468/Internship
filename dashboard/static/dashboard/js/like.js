var likecount = document.getElementById("like")
var count = 0 
function like(){

    count = count + 1;
    if (count%2 === 0){
        likecount.innerHTML = `<i class="fa-solid fa-heart fa-xl" style="color: #011b1d;"></i>`
    }
    else{
        likecount.innerHTML = `<i class="fa-regular fa-heart fa-xl" style="color: #011b1d;"></i>`

    }
    
}