#include <iostream>
#include <windows.h> //Funciones para limpiar consola y cerrar ventanas
#include <stdlib.h> //Importa Random
#include <time.h> //Semilla del random
#include <winbgim.h> //Modo gráfico de Borland
#include <istream> //Trabajan con strings
#include <sstream>
#include <string> //Importa los strings
#include <climits>
#include "include/Laberinto.h"

#define MAXFILAS 28  //MIN 4 ! MAX N Visible ( 28 )
#define MAXCOLUM 65 //MIN 3 ! MAX N Visible ( 65 )
#define CANTHINT 1 //MIN 1 ! MAX N Visible ( 15 )
#define OBJETOS true // true o false

using namespace std;

int fila = 0;
int column = 0;
int numy = 0;
int numx = 0;
int numHint = CANTHINT;
Jugador* player = new Jugador();

//---------------------------------------------------------------------------------------------------------------------------
//Funciones numéricas
//---------------------------------------------------------------------------------------------------------------------------
//Indica la coordenada donde imprimir rectángulo
int coordenada(int num)
{
    return 30+(20*num);
}

//Genera numeros random para los objetos
void generandobj(Nodo** matriz,int fila, int columna)
{
    int x,y,z;
    x = y = z = 0;
    while (x == y || x == z || y == z || x == 0 || y == 0 || z == 0)
    {
        x = rand()%fila; //RECORDAR CAMBIAR NUMERO DEL MODULO DE ACUERDO A LA CANTIDAD DE FILAS
        y = rand()%fila;
        z = rand()%fila;
    }
    matriz[x][rand()%columna].setObjeto(true); //RECORDAR CAMBIAR NUMERO DEL MODULO DE ACUERDO A LA CANTIDAD DE COLUMNAS
    matriz[y][rand()%columna].setObjeto(true);
    matriz[z][rand()%columna].setObjeto(true);

}

//Funcion que confirma que lo insertado en caracteres es un numero
bool esNumero(string element)
{
    int j = 0;
    int i;
    if(element.length()==0)  //Si elemento insertado no existe, retorna falso
    {
        return false;
    }
    else
    {
        int e = element.length();
        for(i =0; i< e; i++)
        {
            if(element.at(i)=='0'||element.at(i)=='1'||element.at(i)=='2'||element.at(i)=='3'||
                    element.at(i)=='4'||element.at(i)=='5'||element.at(i)=='6'||element.at(i)=='7'||
                    element.at(i)=='8'||element.at(i)=='9') //Si posicion del elemento es igual a algun digito, se suma 1
            {
                j++;
            }
        }
        return j==i; //Retorna true si todos los caracteres son digitos, y false si al menos tiene un caracter que no es digito
    }
}

//---------------------------------------------------------------------------------------------------------------------------
//Funciones de interfaz
//---------------------------------------------------------------------------------------------------------------------------
//Borra objeto encontrado dentro del laberinto
void borrarobjeto(bool objeto, Nodo** matriz, int posx, int posy, Jugador* player)
{
    if (objeto)
    {
        matriz[posx][posy].setObjeto(false);
        player->addColectados();
        cout << player->getColectados() << endl;
    }
}

//Actualiza posición del jugador dentro del laberinto
void buscarjugador(Nodo** matriz, int fila, int columna)
{
    for (numy = 0; numy<fila; numy++) //RECORDAR CAMBIARLO DE ACUERDO AL NUMERO DE FILAS
    {
        for (numx = 0; numx<columna; numx++)  //RECORDAR CAMBIARLO DE ACUERDO AL NUMERO DE COLUMNAS
        {
            if (matriz[numy][numx].hayJugador())
            {
                circle(coordenada(numx),coordenada(numy),5);
                setfillstyle(1,4);
                fillellipse(coordenada(numx),coordenada(numy),5,5);
            }
        }
    }
}

//Crea el laberinto
void actualizamatriz(Nodo** matriz, int fila, int columna)
{
        setcolor(1);
        setfillstyle(1,1);
        //CAMINOS HORIZONTALES
        for (numy = 0; numy<fila; numy++)  //RECORDAR CAMBIARLO DE ACUERDO AL NUMERO DE FILAS
            {
                for (numx = 0; numx<columna; numx++) //RECORDAR CAMBIARLO DE ACUERDO AL NUMERO DE COLUMNAS
                {
                    if (matriz[numy][numx].hayCamDer())
                    {
                        int* coord = new int[8];
                        coord[0] = coordenada(numx)-5; //[3]
                        coord[1] = coordenada(numy)-5; //[7]
                        coord[2] = coordenada(numx+1)+5; //[4]
                        coord[3] = coordenada(numy)-5; //[0]
                        coord[4] = coordenada(numx+1)+5; //[2]
                        coord[5] = coordenada(numy)+5; //[3]
                        coord[6] = coordenada(numx)-5; //[2]
                        coord[7] = coordenada(numy)+5; //[1]
                        fillpoly(4,coord);
                    }
                }

            }
        //CAMINOS VERTICALES
        for (numy = 0; numy<fila; numy++)  //RECORDAR CAMBIARLO DE ACUERDO AL NUMERO DE FILAS
            {
                for (numx = 0; numx<columna; numx++)  //RECORDAR CAMBIARLO DE ACUERDO AL NUMERO DE COLUMNAS
                {
                    if (matriz[numy][numx].hayCamAbajo())
                    {
                        int* coord = new int[8];
                        coord[0] = coordenada(numx)-5; //[3]
                        coord[1] = coordenada(numy)-5; //[7]
                        coord[2] = coordenada(numx)+5; //[4]
                        coord[3] = coordenada(numy)-5; //[0]
                        coord[4] = coordenada(numx)+5; //[2]
                        coord[5] = coordenada(numy+1)+5; //[3]
                        coord[6] = coordenada(numx)-5; //[2]
                        coord[7] = coordenada(numy+1)+5; //[1]
                        fillpoly(4,coord);
                    }
                }
            }
        //OBJETOS
        for (numy = 0; numy<fila; numy++)  //RECORDAR CAMBIARLO DE ACUERDO AL NUMERO DE FILAS
            {
                for (numx = 0; numx<columna; numx++)  //RECORDAR CAMBIARLO DE ACUERDO AL NUMERO DE COLUMNAS
                {
                    if (matriz[numy][numx].hayObjeto())
                    {
                        setcolor(3);
                        setfillstyle(1,3);
                        fillellipse(coordenada(numx),coordenada(numy),5,5);
                    }
                }
            }
        setcolor(15);
}

//Menu de ayuda del juego
void menayu()
{
    cleardevice();//Limpia ventana
    settextstyle(0,HORIZ_DIR,2);
    setcolor(15);
    outtextxy(520,60, "            ____");
    outtextxy(520,80, "           /    |");
    outtextxy(520,100,"          [.[.]-|");
    outtextxy(520,120, "          /_   /|");
    outtextxy(520,140,"           {-} | =X ");
    setcolor(4);
    outtextxy(520,160,"         ___    ____");
    outtextxy(520,180,"        /           | ");
    outtextxy(520,200,"       |  |      |  |");
    outtextxy(520,220,"       |__|  ^   |__|");
    outtextxy(520,240,"        | |< O > | | ");
    outtextxy(520,260,"        | |  v   | | ");
    outtextxy(520,280,"        |_|______|_| ");
    setcolor(6);
    outtextxy(520,440,"         _ __ ___ ");
    outtextxy(520,460,"        (____|___)");
    setcolor(1);
    outtextxy(520,300,"          |     _|");
    outtextxy(520,320,"          |  | |-|");
    outtextxy(520,340,"          |  | |_|");
    outtextxy(520,360,"          |  |   |");
    outtextxy(520,380,"          |  |   |");
    outtextxy(520,400,"          |  |   |");
    outtextxy(520,420,"          |  |   |");
    outtextxy(520,430,"          |  |   |");
    setcolor(15);
    outtextxy(520,155,"            #  |");
    outtextxy(520,300,"         W|      |W");
    setcolor(15);
    outtextxy(1,20, " .-------------------------------------.");
    outtextxy(1,40, "(Bienvenido al laberinto! Acá debes so- )");
    outtextxy(1,60, "(brevivir al reto de la vaca Pancho:Con-)");
    outtextxy(1,80, "(seguir los tesoros y salir vivo en el  )");
    outtextxy(1,100,"(intento!                               --¬");
    outtextxy(1,120,"(                                         |");
    outtextxy(1,140,"(Puedes utilizar las tres ayudas, que yo---");
    outtextxy(1,160,"(Sir Makarov puedo brindarte, sin embar-)");
    outtextxy(1,180,"(go, si utilizas más de la cuenta, per- )");
    outtextxy(1,200,"(derás su alma en el vacío!             )");
    outtextxy(1,220,"(                                       )");
    outtextxy(1,240,"(Recuerde, para salir, debes recolectar )");
    outtextxy(1,260,"(los tesoros, sino vivirás atrapado acá )");
    outtextxy(1,280,"((Bueno, puedes salir del juego apretan-)");
    outtextxy(1,300,"(do el botón de End/Fin.                )");
    outtextxy(1,320," ._____________________________________.");
    outtextxy(2,370,"                  .--------------.");
    outtextxy(2,390,"                 (Hola, soy Pancho )");
    outtextxy(2,410,"          (__)   (y puedo hablar...)");
    outtextxy(2,430,"         .(oo).  (Muuuuuuuuuuu...  )");
    outtextxy(2,450,"   /-----|____|---.------------.");
    outtextxy(2,470,"  / |     ||");
    outtextxy(2,490,"	    ||----||");
    outtextxy(2,510,"	    ^^    ^^");
    getch();
}

//Interfaz principal del juego
void intprin()
{
    settextstyle(0,HORIZ_DIR,1);
    setcolor(4);
    outtextxy(100,20,"db       .d8b.  d8888b. d88888b d8888b. d888888b d8b   db d888888b  .d88b. ");
    outtextxy(100,30,"88      d8' `8b 88  `8D 88'     88  `8D   `88'   888o  88 `~~88~~' .8P  Y8.");
    outtextxy(100,40,"88      88ooo88 88oooY' 88ooooo 88oobY'    88    88V8o 88    88    88    88 ");
    outtextxy(100,50,"88      88~~~88 88~~~b. 88~~~~~ 88`8b      88    88 V8o88    88    88    88 ");
    outtextxy(100,60,"88booo. 88   88 88   8D 88.     88 `88.   .88.   88  V888    88    `8b  d8' ");
    outtextxy(100,70,"Y88888P YP   YP Y8888P' Y88888P 88   YD Y888888P VP   V8P    YP     `Y88P'  ");
    setcolor(15);
    outtextxy(80,150, "                                        :.");
    outtextxy(80,160, "                                       .R$.");
    outtextxy(80,170,"                                      :!!!M.");
    outtextxy(80,180,"                                     .?~`~!$.");
    outtextxy(80,190,"                                    .$!' `~!M.");
    outtextxy(80,200,"                                   .$!'   `~!$.");
    outtextxy(80,210,"                                  .$!'     `~!!.");
    outtextxy(80,220,"                                 .$!'       `~!$.");
    outtextxy(80,230,"                                .$!'         `~!$.");
    outtextxy(80,240,"                               .$!'         ~~~!!M.");
    outtextxy(80,250,"                              .$!'mmmxxxx~~~~~~~!!M.");
    outtextxy(80,260,"                          __--@MMM####%%%%~~~~~~~!MM.");
    outtextxy(80,270,"                    __--~~  .$!' `""%%%%%%%%%~~~~~~~!MX.");
    outtextxy(80,280,"              __--~~       .$!'              `~~~~~!MX.");
    outtextxy(80,290,"        __--~~            .$!'                    `~!MM.");
    outtextxy(80,300,"  __--~~                 .$!'                       `!!R.");
    outtextxy(80,310," ~                      .$!'                         `!!M.");
    outtextxy(80,320,"                       .$!'                           `!!R.");
    outtextxy(80,330,"                      .$!'                             `!!8.");
    outtextxy(80,340,"                     .$!'                               `!!N.");
    outtextxy(80,350,"                    .$!:                                 `!!N.");
    outtextxy(80,360,"                   .$!!'                                  `!!&.");
    outtextxy(80,370,"                  .@!!'                                    `!MN.");
    outtextxy(80,380,"                 .$!!'                                      `!M&.");
    outtextxy(80,390,"                .@$MHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!H$N.");
    setcolor(4);
    outtextxy(480,230,"mmm___");
    outtextxy(552,240,"mmm___");
    outtextxy(624,250,"mmm___");
    outtextxy(696,260,"m");
    setcolor(12);
    outtextxy(487,240,"MMMMMMMM");
    outtextxy(527,250,"MMMMMMMMMMMM");
    outtextxy(599,260,"MMMMMMMMMMMM");
    outtextxy(671,270,"MMMM");
    setcolor(14);
    outtextxy(495,250,"NNNN");
    outtextxy(511,260,"NNNNNNNNNNN");
    outtextxy(583,270,"NNNNNNNNNNN");
    outtextxy(655,280,"NNNNNN");
    outtextxy(695,290,"N");
    setcolor(2);
    outtextxy(503,260,"R");
    outtextxy(511,270,"RRRRRRRRR");
    outtextxy(559,280,"RRRRRRRRRRRR");
    outtextxy(639,290,"RRRRRRR");
    outtextxy(680,300,"RRR");
    setcolor(11);
    outtextxy(518,280,"CCCCCCC");
    outtextxy(574,290,"CCCCCCCC");
    outtextxy(623,300,"CCCCCCC");
    outtextxy(663,310,"CCCCC");
    outtextxy(696,320,"C");
    setcolor(1);
    outtextxy(526,290,"GGGGGG");
    outtextxy(559,300,"GGGGGGGG");
    outtextxy(591,310,"GGGGGGGGG");
    outtextxy(623,320,"GGGGGGGGG");
    outtextxy(655,330,"GGGGGG");
    outtextxy(687,340,"GG");
    setcolor(5);
    outtextxy(543,300,"PP");
    outtextxy(575,310,"PP");
    outtextxy(607,320,"PP");
    outtextxy(639,330,"PP");
    outtextxy(671,340,"PP");
}

//Menu principal del juego
void menuprin()
{
    cleardevice();
    intprin(); //Invoca interfaz principal
    setcolor(15);
    settextstyle(0,HORIZ_DIR,3);
    outtextxy(150,440,"j: Jugar una partida!");
    outtextxy(150,480,"a: Ayuda");
    outtextxy(150,520,"s: Salir");
}

//Funcion que muestra en pantalla, caso el usuario use más de tres ayudas, que ha muerto
void hasmuerto()
{
    cleardevice();
    setcolor(15);
    settextstyle(0,HORIZ_DIR,5);
    outtextxy(150,10,"HAS MUERTO :-(");
    settextstyle(0,HORIZ_DIR,2);
    outtextxy(10,100,"     .... NO! ...                  ... MNO! ...");
    outtextxy(10,120,"   ..... MNO!! ...................... MNNOO! ...");
    outtextxy(10,140," ..... MMNO! ......................... MNNOO!! .");
    outtextxy(10,160,"..... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .");
    outtextxy(10,180," ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....");
    outtextxy(10,200,"    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...");
    outtextxy(10,220,"   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....");
    outtextxy(10,240,"   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...");
    outtextxy(10,260,"    ....... MMMMM..    OPPMMP    .,OMI! ....");
    outtextxy(10,280,"     ...... MMMM::   o.,OPMP,.o   ::I!! ...");
    outtextxy(10,300,"         .... NNM:::.,,OOPM!P,.::::!! ....");
    outtextxy(10,320,"          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....");
    outtextxy(10,340,"         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....");
    outtextxy(10,360,"           .. MMMMMNNOOMMNNIIIPPPOO!! ......");
    outtextxy(10,380,"          ...... MMMONNMMNNNIIIOO!..........");
    outtextxy(10,400,"       ....... MN MOMMMNNNIIIIIO! OO ..........");
    outtextxy(10,420,"    ......... MNO! IiiiiiiiiiiiI OOOO ...........");
    outtextxy(10,440,"  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........");
    outtextxy(10,460,"   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........");
    outtextxy(10,480,"   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........");
    outtextxy(10,500,"      ...... OO! ................. ON! .......");
    outtextxy(10,520,"         ................................");
    getch();
    closegraph();
    system("cls");
    exit(0);
}
void auxJuego(int,int);

//Funcion que muestra en pantalla, caso el usuario gane la partida, que ha ganado
void hasganado(int fila, int column)
{
    cleardevice();
    setcolor(15);
    settextstyle(0,HORIZ_DIR,5);
    outtextxy(10,20," .------------------.");
    outtextxy(10,70,"(       YOU WIN! :)  )");
    outtextxy(10,120,"((MUUUUUUUUUUUUU!!! ))");
    outtextxy(10,170," .__________________.");
    outtextxy(2,230,"          (__)");
    outtextxy(2,280,"         .(oo).");
    outtextxy(2,330,"   /-----|____|");
    outtextxy(2,380,"  / |     ||");
    outtextxy(2,430,"	    ||----||");
    outtextxy(2,480,"	    ^^    ^^");
    settextstyle(0,HORIZ_DIR,2);
    getch();
    closegraph();
    system("cls");
    auxJuego(fila,column);
    cleardevice();
    //exit(0);
}
//Funcion que muestra instrucciones y hints en el juego
void pantjuego(Jugador* jugador)
{
    setcolor(15);
    settextstyle(0,HORIZ_DIR,2);
    outtextxy(20,600,"Hints:");
    if (jugador->getCantPistas() == 0)
    {
        outtextxy(120,600,"La próxima morirás...");
    }
    else
    {
        int x = 120;
        for (int i = 0; i < jugador->getCantPistas(); i++)
        {
            outtextxy(x,600,"O");
            x += 30;
        }
    }
    if(OBJETOS){
      outtextxy(20,620,"Objetos colectados: ");
      outtextxy(1,640,"(Debes recolectar tres para salir)");
    char colectados[5];
    itoa(jugador->getColectados(),colectados,10);
    outtextxy(430,620,colectados);
    }

    outtextxy(590,600, "Pg. Dw = Hints");
    outtextxy(590,620, "End = Salir");
    outtextxy(590,640, "Teclas dir. = Mover personaje");
}

//Funcion que pide datos
void juegoprin()
{
    player->setNumPistas(CANTHINT);
    system("cls");
    DestroyWindow(GetActiveWindow()); //Destruye ventana de interfaz
    cout<<"BIENVENIDO AL GENERADOR DE LABERINTOS!"<<endl;
    char cantF[256];
    char cantC[256];
    string cantFilas = "";
    string cantColumn = "";
    while(!esNumero(cantFilas)) //Pide char con numero de filas
    {
        cout <<"Introduzca cant. filas (Minimo 4, maximo 28)"<< endl;
        cin.getline(cantF,256);
        char *charF = &cantF[0];
        cantFilas = charF;
    }
    istringstream (cantFilas) >> fila;
    while (!esNumero(cantColumn))
    {
        cout <<"Introduzca cant. columnas (Minimo 4, maximo 65)"<< endl;
        cin.getline(cantC,256);
        char *charC = &cantC[0];
        cantColumn = charC;
    }
    istringstream (cantColumn) >> column;
    auxJuego(fila,column);
}
void auxJuego(int fila,int column){
    player->setColectados(0);
    player->setNumPistas(1);
    if(fila>3 && fila<=MAXFILAS && column>2 && column<=MAXCOLUM){
        cout<<"DISFRUTE SU ESTANCIA!"<<endl;
        Laberinto* lab = new Laberinto(fila,column); //MODIFICAR CANTIDAD DE ELEMENTOS QUE PRODUCE LABERINTO
        lab->depthSearch();
        initwindow(1100,700);
        Nodo** matr = lab->getGrafo();
        srand(time(NULL));
        if(OBJETOS){
           generandobj(matr,fila,column);
        }
        bool cond = false;
        int posy = 0;
        int posx = 0;
        matr[posx][posy].setJugador(player);
        //lab->getMatrizLab();
        //lab->imprimirGrafo();

        while (!cond)
        {
            pantjuego(player);
            actualizamatriz(matr, fila, column);
            buscarjugador(matr, fila, column);
            if(OBJETOS){
                if (matr[fila-1][column-1].hayJugador() && (player->getColectados() == 3))
                {
                        hasganado(fila,column);
                }
            }else{
                if (matr[fila-1][column-1].hayJugador())
                {
                        hasganado(fila,column);
                }
            }
            int option = getch();
            putch(option);
            if (option == 72) //ARRIBA
            {
                if (matr[posx][posy].hayCamArriba())
                {
                    matr[posx][posy].setJugador(NULL);
                    matr[posx-1][posy].setJugador(player);
                    posx--;
                    borrarobjeto(matr[posx][posy].hayObjeto(),matr,posx,posy, player);
                }
            }
            if (option == 75) //IZQ
            {
                if (matr[posx][posy].hayCamIzq())
                {
                    matr[posx][posy].setJugador(NULL);
                    matr[posx][posy-1].setJugador(player);
                    posy--;
                    borrarobjeto(matr[posx][posy].hayObjeto(),matr,posx,posy, player);
                }
            }
            if (option == 77) //DER
            {
                if (matr[posx][posy].hayCamDer())
                {
                    matr[posx][posy].setJugador(NULL);
                    matr[posx][posy+1].setJugador(player);
                    posy++;
                    borrarobjeto(matr[posx][posy].hayObjeto(),matr,posx,posy, player);
                }
            }
            if (option == 80) //ABAJO
            {
                if (matr[posx][posy].hayCamAbajo())
                {
                    matr[posx][posy].setJugador(NULL);
                    matr[posx+1][posy].setJugador(player);
                    posx++;
                    borrarobjeto(matr[posx][posy].hayObjeto(),matr,posx,posy, player);
                }
            }
            if (option == 79)
            {
                closegraph();
                exit(0);
            }
            if (option == 81)
            {
                if (player->getCantPistas() == 0)
                {
                    player->die();
                    hasmuerto();
                }
                else
                {
                    player->removePista();
                    cleardevice();
                }
            }
        }
    }else{
        cout<<"NO PUEDE INGRESAR. INTENTELO DE NUEVO"<<endl;
        cout<<"CON OTROS PARAMETROS"<<endl;
        cout<<""<<endl;
        juegoprin();
    }

}

//Función que ejecuta programa
int main()
{
    initwindow (850,600);
    //movimiento(30,30);
    //getch();
    char c;
    while (c != 's'){
        menuprin();
        c = getch();
        putch(c);
        switch(c){
            case 'a':
                menayu();
                break;
            case 'j':
                juegoprin();
                c = 's';
                break;
        }
    }
    system("cls");
    closegraph();
    return 0;
}
