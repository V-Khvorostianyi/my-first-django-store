
$(document).ready(function() {
    var form;
    form = $('#form_buying_product');
    console.log(form);


    function basketUpdating(product_id, qty, is_delete) {
        var data = {};
        data.product_id = product_id;
        data.qty = qty;
        var csrf_token = $('#form_buying_product').find('[name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete) {
            data["is_delete"] = true;
        }

        var url = form.attr("action");

        console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.products_total_nmb);
                if (data.products_total_nmb || data.products_total_nmb == 0) {
                    $('#basket_total_nmb').text("(" + data.products_total_nmb + ")");
                    console.log(data.products);
                    $('.basket-items ul').html("");
                    $.each(data.products, function (k, v) {

                        $('.basket-item').append('<li>' + v.name + ', qty: ' + v.qty + ', total price: ' + v.price * v.qty + 'UAH' + '<a href="" id="id-delete_item" class="delete_item" data-product_id="' + v.id + '" >x</a>' + '</li>');
                    });

                }

            },
            error: function () {
                console.log("error")
            }
        })

    }


    form.on('submit', function (e) {
        e.preventDefault();
        var qty = $('#number').val();
        var submit_btn = $('#submit-btn');
        var name = submit_btn.data('name');
        var product_id = submit_btn.data('product_id');
        var product_price = submit_btn.data('price');
        basketUpdating(product_id, qty, is_delete = false)

    });

    function showingBasket() {
        $('.basket-items').removeClass('hidden');
    };


    $(document).on('click', '.delete_item', function (e) {
        e.preventDefault();
        $(this).closest('li').remove();


    })
});

