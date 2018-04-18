#include <stdio.h>



void crack(){
		printf("CRACKED!!!!!!\n");
}


int main(int args,char *argv[]){

		int zero = 0;
		char buf[10];

		printf("buf address\t=\t%x\n",(int)buf);
		printf("zero address\t=\t%x\n",(int)&zero);
		printf("------------------------------------- \n");


		fgets(buf,64,stdin);

		 
		printf("zero address\t=\t%x\n",zero);
		if (zero == 0x99999999){
				printf("\n");
				crack();
				printf("\n");
		}else if (zero == 0x12345678){
				while(1){
						crack();
				}
		}else if (zero == 0){
		printf("--------Succeeded normally!!!---------\n");
		}else
		return 0;
}
