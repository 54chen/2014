  #!/bin/bash
  for file in `find . -type f|grep -v .git|grep -v .png|grep -v .css|grep -v .js|grep -v pro.sh|grep -v 1.txt|grep -v 2.txt|grep -v assets`
  do
  	echo $file
	#file2=${file/twitter/weibo}
	#sed -i '' 's/name\=\"q\"\ placeholder\=\"Search\"/name\=\"key\"\ placeholder\=\"Search\"/g' $file
	sed -i '' 's/"http\:\/\/www\.54chen\.com\" style="/"http\:\/\/blog\.54chen\.com\" style="color\:white;/g' $file
	sed -i '' 's/想找旧版内容/想找最新内容/g' $file


	#mv $( dirname "$file" ) $( dirname "$file2" )
	#sed -i '' 's/twitter/weibo/g' $file
	#grep -H weibo $file
	#sed -i '' 's/http\:\/\/www\.54chen\.com\/wp-content\/themes\/54chen2011//g' $file  
	#mkdir -p /tmp/$( dirname "$file" )
  	#diff -w 1.txt $file|grep \^\>|awk -F \^\> '{print $2}' > /tmp/$file
  	#diff -w 2.txt /tmp/$file | grep \^\>|awk -F \^\> '{print $2}' > /tmp/$file.2
  	#cat /tmp/$file.2 > $file 
  	#rm -rf /tmp/$( dirname "$file" )
  done
