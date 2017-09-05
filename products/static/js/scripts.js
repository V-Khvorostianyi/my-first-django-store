
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
        // console.log(name);
        // console.log(product_id);
        // console.log(product_price);

        var data ={};
        data.product_id = product_id;
        data.qty = qty;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr('action');
        console.log(data)
        $.ajax({
            url : url,
            type : 'POST',
            data : data,
            cache :true,
            success:function (data) {
                console.log('OK');
                console.log(data.products_total_qty);
                // if (data.products_total_qty) {
                //     $('#card_total_orders').text("("+data.products_total_qty+")");
                // }
            },
            error:function () {
                console.log('error');
            }
        });
        // language=HTML
        $('.basket-item').append('<li>'+name+', qty: ' + qty +', total price: '+product_price*qty+'UAH'+'<a href="" id="id-delete_item" class="delete_item" >x</a>'+'</li>');
    });
    $(document).on('click','.delete_item', function (e) {
        e.preventDefault();
        $(this).closest('li').remove();


    })
});
