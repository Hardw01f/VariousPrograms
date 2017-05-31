/* ********************************** */
/* sample program of tcp-server v0.94 */
/*   for basic-network-programming    */
/*              by T.Nagata.          */
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

int main(int argc, char *argv[])
{

  int s;                      /* file descriptor for socket */
  int n;                      /* bytes of message */
  struct sockaddr_storage ss; /* address of server */
  int len;                    /* length of address */
  char mesg[BUFFER];          /* message words */
  char recv_buf[BUFFER] ;     /* recieve buffer */
  char send_buf[BUFFER];      /* send buffer */

  /* check of argument */

  if (argc != 2) {
    fprintf(stderr, "Usage: %s (port) \n", argv[0]);
    exit(EXIT_FAILURE);   /*処理失敗*/
  }

  /* create and bind socket */

  s = make_socket(argv[1]);   /*socket作成*/

  /* waiting for connection */

  listen(s, 5);   /*FDの監視,受信待機*/

  /* main loop */

  while (1) {

    /* accept of connection */

    /*clientのアドレスを受け取り新しいソケットのFDを作成する*/
    len = sizeof(ss);
    if ((s = accept(s, (struct sockaddr*) &ss, &len)) < 0) { 
      perror("accept");
      exit(EXIT_FAILURE);  /*処理失敗*/
    }

    while (1) {
      int i = 0;  /* count of receiving character */

      n = sprintf(send_buf, "TCP> ");  /*send_bufに"TCP> "を格納*/
      send(s, send_buf, n, 0);   /*接続したsocketにデータを送信する*/

      /* data processing of stream type */

      for(i=0; i < BUFFER - 1; i++){
        if ((recv(s, &recv_buf[i], 1, 0)) < 0){   /*接続したsocketからのデータ受信*/
          perror("while receiving data");  /*　待機中　*/
	  break;
        }
	
        /* recieve processing by new-line */

        if (recv_buf[i] == '\n') {
          break;
        }
      }

      recv_buf[i] = '\0';                  /*NULL*/
      printf("receive '%s'\n", recv_buf);  /*受信したデータの出力*/

      /* process of recieving message */

      if((sscanf(recv_buf, "%s", mesg)) <= 0)   /*mesgが0以下,指定された文字以外の時continue*/
	continue;

      n = sprintf(send_buf, "%s\n", mesg);  /*mesgの文字数を取得*/

      if (n == 0)
        n = sprintf(send_buf, "\n"); /*n==0の時は改行する*/

      if (send(s, send_buf, n, 0) < 0)   /*socketへのデータ送信が失敗の場合*/
        break;
      printf("send %s", send_buf);

    }
    printf("connection closed.\n");
    close(s);   /*socket通信終了*/

  }
  return(EXIT_SUCCESS);  /*通信成功*/

}

int make_socket(const char *port)
{

  struct addrinfo hints;     /* address of server */
  struct addrinfo *ai;       /* address information */
  int s;                     /* file descriptor for socket */

  /* resolve of server's IP address */

  memset(&hints, 0, sizeof(hints)); /*hintsの初期化*/
  hints.ai_family = AF_UNSPEC;      /*IPv4でもIPv6の両方に対応可能*/
  hints.ai_socktype = SOCK_STREAM;  /*sockettype*/
  hints.ai_flags = AI_PASSIVE;     /*host名がNULLの場合,acceptするsocketをbindに適した形にする*/
  if ((getaddrinfo(NULL, port, &hints, &ai)) != 0) {   /*socketに関する情報の関連付け*/
    fprintf(stderr, "can't resolve address\n");        /*失敗した場合*/
    exit(EXIT_FAILURE);                                /*処理失敗*/
  }

  /* create socket */

  if ((s = socket(ai->ai_family, ai->ai_socktype, 0)) < 0) { /*socketの作成*/
    perror("socket");
    exit(EXIT_FAILURE); /*処理失敗*/
  }

  /* bind socket */

  if (bind(s, ai->ai_addr, ai->ai_addrlen) < 0) {  /*ソケットへのアドレス関連付け*/
    perror("bind");
    exit(EXIT_FAILURE); /*処理失敗*/
  }

  freeaddrinfo(ai);   /*サーバーアドレス情報の解放*/
  return(s);        /*socketを返す*/

}
