/**
 * Created by avathar on 4/23/2015.
 */


$(function(){
    $('.match-input').hide();
    $('a.games').click(function(e){
        e.preventDefault();
        $('.match-input').slideToggle();
    });
});