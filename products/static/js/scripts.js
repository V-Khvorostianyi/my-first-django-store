
$(document).ready(function() {
    var form;
    form = $('#form_buying_product');
    console.log(form);
    form.on('submit',function (e) {
        e.preventDefault();
        var qty = $('#number').val();
        console.log(qty);
        var submit_btn = $('#submit-btn');
        var name = submit_btn.data('name');
        var product_id = submit_btn.data('product_id');
        var product_price = submit_btn.data('price');
        console.log(name);
        console.log(product_id);
        console.log(product_price);
        // language=HTML
        $('ul.basket-item').append('<li>"+name+", qty: ' + qty +', total price: '+product_price*qty+'UAH<a class="delete_item">x</a></li>');

    $(document).on('click','.delete_item', function () {
        $(this).closest('li').remove();

        
    })
});
