$("#fieldset-inscricao").slideDown("slow");
$(".descricao-tipo").html($("#id_tipo").find("option[selected]").text());

var atividades_selecionadas = $("#id_atividades").find("option[selected]"); //retorna todas as atividades selecionadas
var html_descricao_atividades = "";
var total = 0;
for(i=0, len = atividades_selecionadas.length; i < len; i++){
    html_descricao_atividades += "<p> <b>"+(i+1)+": </b>"+atividades_selecionadas[i].text+"</p>";

    total += parseFloat($("#valor_atividade_"+atividades_selecionadas[i].value).html());
}

$("#descricao-atividades").html(html_descricao_atividades);
$("#valor-total-atividades").html(number_format(total, 2, ',', '.'));