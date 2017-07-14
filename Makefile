run:
	openresty -c `pwd`/nginx-sans-rate.conf

rated:
	openresty -c `pwd`/nginx.conf


