(function($) {

    $("#pricipal-slide").slider({
        range: "min",
        min: 1000,
        max: 15000,
        value: 15000,
        step: 1000,
        slide: function(event, ui) {
            $("#pricipal").text(ui.value);
            loancalculate();
        }
    });
    $("#pricipal").text($("#pricipal-slide").slider("value"));

    $("#totalyear-slide").slider({
        range: "min",
        min: 3,
        max: 12,
        step: 3,
        value: 12,
        slide: function(event, ui) {
            $("#totalyear").text(ui.value);
            loancalculate();
        }
    });
    $("#totalyear").text($("#totalyear-slide").slider("value"));

    $("#intrest-slide").slider({
        range: "min",
        min: 6.10,
        max: 328.55,
        step: 0.01,
        value: 328.55,
        slide: function(event, ui) {
            $("#intrest").text(ui.value);
            loancalculate();
        }
    });
    $("#intrest").text($("#intrest-slide").slider("value"));

    loancalculate();
})(jQuery);

function loancalculate()
{
    var loanAmount =$("#pricipal").text();
    var numberOfMonths =$("#totalyear").text();

    if (numberOfMonths == 12){
      var rateOfInterest=328.55;
    }else if (numberOfMonths == 9){
      var rateOfInterest=344.6;
    }else if (numberOfMonths == 6){
      var rateOfInterest=364.4;
    }else if (numberOfMonths == 3){
      var rateOfInterest=381.7;
    }


    //var rateOfInterest=$("#intrest").text();

    var monthlyInterestRatio = (rateOfInterest/100)/12;

    var top = Math.pow((1+monthlyInterestRatio),numberOfMonths);
    var bottom = top -1;
    var sp = top / bottom;
    var emi = Math.round(((loanAmount * monthlyInterestRatio) * sp));
    var full = numberOfMonths * emi;
    var interest = full - loanAmount;
    var int_pge =  (interest / full) * 100;
    //$("#tbl_int_pge").html(int_pge.toFixed(2)+" %");
    //$("#tbl_loan_pge").html((100-int_pge.toFixed(2))+" %");

    var emi_str = emi.toFixed(2).toString().replace(/,/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    var loanAmount_str = loanAmount.toString().replace(/,/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    var full_str = full.toFixed(2).toString().replace(/,/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    var int_str = interest.toFixed(2).toString().replace(/,/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");


    $("#emi").html(emi_str);
    $("#tbl_emi").html(int_str);
    $("#tbl_la").html(full_str);
}
