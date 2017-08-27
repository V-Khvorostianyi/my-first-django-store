
$(document).ready(function() {
    var form;
    form = $('#form_buying_product');
    console.log(form);
    form.on('submit',function (e) {
        e.preventDefault();
        console.log('123');
        var qty = $('#number').val();
        console.log(qty);
    });
});
