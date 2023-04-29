(function () {
    var commercialIndex = 1;
    var addCommercialButton = document.getElementById("addRow");
    var commercialsDiv = document.getElementById("commercials");

    addCommercialButton.addEventListener("click", function () {
        var commercialDiv = document.createElement("div");
        commercialDiv.classList.add("commercial");

        commercialDiv.innerHTML =
            '<input type="email" name="email-' + commercialIndex + '" required>' +
            '<input type="number" max="100" accuracy="2" min="0" id="Percentual" name="percentage-' + commercialIndex + '" style="margin-left:5px;">' +
            '<span class="remove" style="padding-left: 13px;">X</span>';

        var removeButton = commercialDiv.querySelector(".remove");

        removeButton.addEventListener("click", function () {
            commercialDiv.parentNode.removeChild(commercialDiv);
        });

        commercialsDiv.appendChild(commercialDiv);

        commercialIndex++;

    });
})();