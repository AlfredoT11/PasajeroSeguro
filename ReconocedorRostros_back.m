clear,clc,close all
%% ------------------- E N T R E N A M I E N T O -------------------------
load('car_personas2')
personas=4;
fotos=6;
bd=cargar_imagenes(personas,fotos);
%bd=cargar_imagenes();
%% ---------------------------------------
Unos=ones(1,size(bd,2));
media=mean(bd,2);
BDP=single(bd)-(single(media)*single(Unos));
%% ---------------------------------------
%single complesión de datos 8 bits
%double 16 bits
MC=single(BDP)'*single(BDP);
[EF,EV]=eig(MC);
%% ---------------------------------------
RE=single(BDP)*EF; %amplificando lo que más interesa y minimizar lo que no importa
Car=10; %tener los diez valores más grandes -lo escencial-
MR=RE(:,end:-1:end-(Car-1));
%% ---------------------------------------
patron=zeros(size(bd,2),Car);
for i=1:size(bd,2)
    patron(i,:)=single(BDP(:,i))'*MR; 
end
%}
backpatron=zeros(personas,size(patron,2));
%for i=1:personas
    %backpatron(i,:)=strcat('P',num2str(personas);
%end
backpatron(1,:)=persona1;
backpatron(2,:)=persona2;
backpatron(3,:)=persona3;
backpatron(4,:)=persona4;
%% -------------------------- P R U E B A --------------------------------
k=6;
m=1;
%bd2=cargar_imagen(k,m);
%if (isempty(carga))
Base=zeros(12000,6);
for fotos=1:6
    a=imread(strcat('x',num2str(fotos),'.jpg'));
    a=rgb2gray(imresize(a,[120 100]));
    Base(:,fotos)=reshape(a,size(a,1)*size(a,2),1);
end
w=uint8(Base);
bd2=w;

num=ceil((k*m)*rand(1,1));
FA=bd2(:,num);
%% ---------------------------------------
subplot(121),imshow(reshape(FA,120,100));
title('Buscando a...','FontWeight','Bold','Color','Red')
%% ---------------------------------------
subplot(122)
Pru=single(FA)-media;   % Se aplica a una sola imagen
salida=single(Pru)'*MR; % en términos de base de datos
backsalida=back_rostros(salida,1,1);
MS=[];
for i=1:personas
    MS(i,:)=(backpatron(i,:)-backsalida);       
    if (rem(1,5)==1)
        a=0;
        b=23;
        num_rand=ceil(a+(b-a).*rand(1,1));
        imshow(reshape(bd(:,num_rand),120,100));
        %pause(0.05)
    end
    drawnow
end
MS=sum(abs(MS),2);
[A,B]=min(MS);
%disp(num)
a=(B-1)*6+1;
b=(B-1)*6+6;
ima_r=ceil(a+(b-a).*rand(1,1));
subplot(122), imshow(reshape(bd(:,ima_r),120,100));
if B==1
    title('¡Es Danny!')
elseif B==2
    title('¡Es Rodolfo!')
elseif B==3
    title('¡Es Casio!')
else 
    title('¡Es Dafne!')
end
%title('¡E N C O N T R A D O!')