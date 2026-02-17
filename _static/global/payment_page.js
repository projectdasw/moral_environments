// ambil nilai dari backend (aman untuk JS)
let finalApp = JSON.parse('"{{ chosen_app }}"');

let appBox = document.getElementById("app-box");
let spinBtn = document.getElementById("spin-btn");

let dummyApps = ["risk_task", "ambiguity_task", "company_task"];

spinBtn.addEventListener("click", function(){

    spinBtn.disabled = true;
    spinBtn.innerHTML = "Mengacak...";

    let counter = 0;

    let interval = setInterval(function() {

        appBox.innerHTML = dummyApps[Math.floor(Math.random() * dummyApps.length)];
        counter++;

        if (counter > 40) {
            clearInterval(interval);

            // 🔥 tampilkan nilai yang sudah tersimpan di database
            appBox.innerHTML = finalApp;

            spinBtn.style.display = "none";
        }

    }, 80);

});