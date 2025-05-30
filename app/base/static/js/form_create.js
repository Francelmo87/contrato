
$(document).ready(function() {
    // Adicionar novo item
    $('#add-item').click(function() {
        const totalForms = $('#id_items-TOTAL_FORMS');  // Corrigido para 'items'
        const formCount = parseInt(totalForms.val());
        const newFormHtml = $('#item-template').html().replace(/__prefix__/g, formCount);
        
        $('#items-container').append(newFormHtml);
        totalForms.val(formCount + 1);
        
        // Atualiza os IDs e names dos novos campos
        $('#item-' + formCount + ' :input').each(function() {
            const name = $(this).attr('name').replace('__prefix__', formCount);
            const id = $(this).attr('id').replace('__prefix__', formCount);
            $(this).attr({'name': name, 'id': id});
        });
        
        // Remover item
        $('#items-container').on('click', '.remove-item', function() {
            $(this).closest('.item-form').remove();

            // Ajustar TOTAL_FORMS, se necessário:
            const totalForms = $('#id_items-TOTAL_FORMS');
            const formCount = $('#items-container .item-form').length;
            totalForms.val(formCount);
        });
    });
});
