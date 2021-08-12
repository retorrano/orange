
$("#card_number").on('change', function(){
    
    var url = $("#card_number").attr("url") + $(this).val();
    alert(url);
    $.ajax({
        url: url,

        success: function(response){
            $("#name").val(response.name)
            $("#address").val(response.address);
        }
    });
});