/* ********************************** */
/* sample program of tcp-client v0.94 */
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
  struct timeval tv;          /* time value of select */
  fd_set readfd;              /* file descriptor for select */
  char recv_buf[BUFFER];      /* recieve buffer */
  char send_buf[BUFFER];      /* send buffer */

  /* check of argument */
  /*コマンドライン引数の確認*/

  if (argc != 3) {
    fprintf(stderr, "Usage: %s (hostname) (port) \n", argv[0]);
    exit(EXIT_FAILURE);
  }

  /* create socket and connect to server */

  s = connect_server(argv[1], argv[2]);  /*ソケットの作成と接続,FDの作成*/

  /* main loop */

  while (1) {

    /* set of select timeout value */

    tv.tv_sec  = 30;  /*Timeout時間の設定*/
    tv.tv_usec = 0;

    /* check of input from standard input or server */
    /*FDの監視,受信待機,読み込み&書き込み&例外のFDの監視*/

    FD_ZERO(&readfd);   /*readfgを0に*/
    FD_SET(0, &readfd); 
    FD_SET(s, &readfd); /*sとreadfdの関連付け*/
    if ((select(s + 1, &readfd, NULL, NULL, &tv)) <= 0) {
      fprintf(stderr, "\nTimeout\n");
      break;
    }

    /* input from standard input */

    if (FD_ISSET(0, &readfd)) {  /*fdに変化があったか確認*/
      if ((n = read(0, recv_buf, BUFFER - 1)) <= 0)
        break;
      recv_buf[n]='\0';  /*NULL*/
      sscanf(recv_buf, "%s", send_buf); /*recv_bufからの入力をsend_buf*/
      if (strcmp(send_buf, "quit") == 0)   /*文字列比較*/
        break;
      if (send(s, recv_buf, n, 0) <= 0)    /*recv_bufをsocketへ送信*/
        break;
    }

    /* recieve from server */

    if (FD_ISSET(s, &readfd)) { /*fdに変化があったかの確認*/
      if ((n = recv(s, recv_buf, BUFFER - 1, 0)) <= 0) {  /*データを受け取りそのbyte数を返す*/
        fprintf(stderr, "connection closed.\n");
        exit(EXIT_FAILURE); /*処理失敗*/
      }
      recv_buf[n]='\0';
      printf("%s", recv_buf);
      fflush(stdout);  /*改行コードがなくてもバッファを出力*/
    }

  }
  strcpy(recv_buf, "quit");  /*quitをrecv_bufにコピー*/
  send(s, recv_buf, n, 0);   /*サーバーに送信*/
  close(s);                  /*socket通信終了*/

  return(EXIT_SUCCESS);

}

int connect_server(const char *hostname, const char *port)
{

  struct addrinfo hints;     /* address of server */
  struct addrinfo *ai;       /* address information */
  int s;                     /* file descriptor for socket */

  /* resolve of server's IP address */

  memset(&hints, 0, sizeof(hints));  /*hintsの初期化*/
  hints.ai_family = AF_UNSPEC;       /*IPv4でもIPv6でも対応可能*/
  hints.ai_socktype = SOCK_STREAM;   /*sockettype*/
  hints.ai_flags = AI_PASSIVE;       /*host名がNULLの場合acceptするsocketをbindしやすくする*/
  if ((getaddrinfo(hostname, port, &hints, &ai)) != 0) { /*ポート,アドレス情報の取得*/
    fprintf(stderr, "can't resolve address\n");
    exit(EXIT_FAILURE); /*処理失敗*/
  }

  /* create socket */

  if ((s = socket(ai->ai_family, ai->ai_socktype, 0)) < 0) {  /*socket作成*/
    perror("socket");
    exit(EXIT_FAILURE);  /*処理失敗*/
  }

  /* connect to server */

  if (connect(s, ai->ai_addr, ai->ai_addrlen) < 0){ /*指定したアドレスでsocketへの接続を試みる*/
    perror("connect");
    exit(EXIT_FAILURE);  /*処理失敗*/
  }
  printf("connected to '%s'\n", hostname);

  freeaddrinfo(ai);  /*アドレス情報の解放*/
  return(s);  /*socketを返す*/

}
