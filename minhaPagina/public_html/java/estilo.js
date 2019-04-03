var b_val = true;
var x=0, y=0,z=0,click=0;
var m,v;
$(document).ready(function(){
    $("#troca").click(function(){
       if(b_val){
           b_val=false;
           $("#midnam").css("display","none");
       }else{
           b_val=true;
           $("#midnam").css("display","inline");
       }
    });
    $("#cair").click(function(){
        if(click === 0){
       $("#linkes").css("position","absolute");
       $("#linkes").css("left","300px");
       x=0;
       m = setInterval(function(){
           x+=1;
           $("#linkes").css("top",x+"px");
           if(x>=800){
               x=800;
           }
           if(x>=200){
                $("#css").css("position","absolute");
                $("#css").css("left","500px");
                y+=1;
                $("#css").css("top",y+"px");
           }
           if(y>=800){
               y=800;
           }
           if(x>=300){
               $("#cabecalho").css("position","absolute");
               $("#cabecalho").css("left","250px");
               z+=1;
               $("#cabecalho").css("top",z+"px");
           }
           if(z>=700){
               clearInterval(m);
           }
        } ,8); 
        }else{
            location.reload();
        }
        click+=1;
    });
    
});