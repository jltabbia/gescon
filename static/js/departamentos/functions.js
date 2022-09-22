function ListaDptos(id) {

    $.ajax({
        url:"/departamentos/listadptos/"+id,
        type:"get",
        dataType:"json",
        success: function(response) {
            console.log(response);
           $.each(function(response, key){
                $("#departamentos").tbody.empty();
                $("#departamentos").tbody.append("<tr><td>"+key.id+"</td></tr>");
            }) 
            //$("#departamentos").dataTable(response);
        }


    });
};

$(document).ready(function(){
    
    $("#edificio_id").change(function() {
        var id=$("#edificio_id").val();
        $("#id_edificio").val(id);
        $("#agrega").empty();
        $("#agrega").append("<a href='agregar' id='agregar' class='btn btn-sm btn-primary mt-3 mb-3'><i class='fa fa-add'></i> Agregar</a>")
        ListaDptos(id);
    }).trigger("change")
});

