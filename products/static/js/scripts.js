
$(document).ready(function() {
    var form;
    form = $('#form_buying_product');
    console.log(form);


    function basketUpdate(product_id,qty, is_delete) {
        var data ={};
        data.product_id = product_id;
        data.qty = qty;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete){
            data["is_delete"] = true;
        }

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
                if (data.products_total_qty || data.products_total_qty==0 ) {
                    $('#card_total_orders').text("("+data.products_total_qty+")");
                    console.log(data.products);
                    $('.basket-item').html("");
                    $.each(data.products,function (key,value) {
                        $('.basket-item').append('<li>'+value.name+', qty: ' + value.qty +', '
                        +'total price: '+value.total_price+'UAH'
                        +'<a href="" id="id-delete_item" class="delete_item"  data-product_id = "'+value.id+'" >x</a>'
                        +'</li>');
                    });
                //ok
                }
            },
            error:function () {
                console.log('error');
            }
        });



    }

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
        basketUpdate(product_id,qty, is_delete=false)

    });
    $(document).on('click','.delete_item', function (e) {
        e.preventDefault();
        $(this).closest('li').remove();
        qty = 0;
        product_id = $(this).data("product_id");
        basketUpdate(product_id,qty, is_delete=true)

    });

    function carculatingBasketAmount() {
        var total_order_amount = 0;
        $('.total_product_in_cart_amount').each(function () {
            total_order_amount +=  parseFloat($(this).text());
    });
        total_order_amount = total_order_amount.toFixed(2);
        $('.total_order_amount').text(total_order_amount+"UAH");
    };

    $(document).on('change', ".product-in-basket-qty", function(){
        var current_nmb = $(this).val();
        console.log(current_nmb);

        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
        console.log(current_price);
        var total_amount = parseFloat(current_nmb*current_price).toFixed(2);
        console.log(total_amount);
        current_tr.find('.total_product_in_cart_amount').text(total_amount);

        carculatingBasketAmount();
    });

    carculatingBasketAmount();
});
