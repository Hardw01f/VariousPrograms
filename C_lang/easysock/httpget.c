/* ********************************** */
/* sample program of tcp-client v0.94 */
/*   for basic-network-programming    */
/*              by T.Nagata.          */
/*               R.Tsukayama          */
/* ********************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netdb.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define BUFFER 1024
#define TRUE 1
#define FALSE 0

int main(int argc, char *argv[])
{

  int s;                      /* file descriptor for socket */
  int n;                      /* bytes of message */
  struct timeval tv;          /* time value of select */
  fd_set readfd;              /* file descriptor for select */
  char recv_buf[BUFFER];      /* recieve buffer */
  char send_buf[BUFFER];      /* send buffer */
  char *HOST_NAME;            
  char *URI_NAME;
  char *tmp[BUFFER];
  int FLAG;

  /* check of argument */
  /* コマンドライン引数の確認*/

  if (argc != 2) {
    fprintf(stderr, "Usage: %s (TargetURL) \n", argv[0]);
    exit(EXIT_FAILURE);
  }

  /* create socket and connect to server */

   HOST_NAME=strtok(argv[1],"/");   /*入力したURLを"/"でくり分解*/

   URI_NAME=strtok(NULL,"\0");      /*NULLに区切り文字を設定*/

   if(URI_NAME ==NULL) {   /*"/"をURIに設定する*/
     strcpy(&URI_NAME,"/"); 
     FLAG = TRUE;
   }else{
     sprintf(tmp,"%s%s","/",URI_NAME);   /*tmpにURI_NAMEのデータの先頭に"/"を入れて格納*/
     strcpy(URI_NAME,tmp);               /*URI_NAMEに返す*/
     FLAG = FALSE;

   }

  s = connect_server(HOST_NAME, "http"); /*httpのポートを使うから*/

  FD_ZERO(&readfd);
  FD_SET(0,&readfd);
  FD_SET(s,&readfd);


   if (FD_ISSET(0, &readfd)) {
                              /*FLAGがtrueであった場合,GETリクエスト及びHost名の送信を行う*/
                              /*リクエストの送信*/
    send(s, "GET ",      strlen("GET "),      0);
    if(FLAG){
    send(s, &URI_NAME,  strlen(&URI_NAME),  0);
    }else{
    send(s, URI_NAME,  strlen(URI_NAME),  0);}
    send(s, " HTTP/1.0\r\n", strlen(" HTTP/1.0\r\n"), 0);
    send(s, "Host: ",    strlen("Host: "),    0);
    send(s,HOST_NAME, strlen(HOST_NAME), 0);
    send(s,"\r\n\r\n",strlen("\r\n\r\n"),0);
}


   if(FD_ISSET(0,&readfd)) {
       while(recv(s,recv_buf,BUFFER -1,0)) {
                               /*recv中はループし続ける*/
         printf("%s",recv_buf);
           memset(&recv_buf,'\0',sizeof(recv_buf));  /*初期化,データの解放*/
       }
     
      printf("%s",recv_buf);  
      printf("\n");
      fflush(stdout);
   }


    /* set of select timeout value */
  close(s);

  return(EXIT_SUCCESS);

}

int connect_server(const char *hostname, const char *port)
{

  struct addrinfo hints;     /* address of server */
  struct addrinfo *ai;       /* address information */
  int s;                     /* file descriptor for socket */

  /* resolve of server's IP address */

  memset(&hints, 0, sizeof(hints));
  hints.ai_family = AF_UNSPEC;
  hints.ai_socktype = SOCK_STREAM;
  hints.ai_flags = AI_PASSIVE;
  if ((getaddrinfo(hostname, port, &hints, &ai)) != 0) {
    fprintf(stderr, "can't resolve address\n");
    exit(EXIT_FAILURE);
  }

  /* create socket */

  if ((s = socket(ai->ai_family, ai->ai_socktype, 0)) < 0) {
    perror("socket");
    exit(EXIT_FAILURE);
  }

  /* connect to server */

  if (connect(s, ai->ai_addr, ai->ai_addrlen) < 0) {
    perror("connect");
    exit(EXIT_FAILURE);
  }
  printf("connected to '%s'\n", hostname);

  freeaddrinfo(ai);
  return(s);

}
