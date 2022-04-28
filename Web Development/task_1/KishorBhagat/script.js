console.log("Script Included");
let item = document.getElementsByClassName("item");
// let close = document.getElementById("close");
for (let image of item) {
    image.addEventListener('click', function () {
        // console.log("Image is Clicked", image);
        // console.log("Image is Clicked", attribute);
        let bigImg = document.getElementById("bigImg");
        bigImg.style.visibility = "visible";
        let attribute = image.getAttribute("src");
        bigImg.innerHTML = `<img src="${attribute}" alt="">`;
        bigImg.innerHTML += `<img src="images/cross.png" alt="" id="cross"/>`;
        bigImg.classList.add("hidden");


        let cross = document.getElementById("cross");
        cross.addEventListener("click", function () {
            // console.log("Closed Click");
            bigImg.style.visibility = "hidden";

        });

    });
}
