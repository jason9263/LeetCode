function fn = fib(n)
	if n==1
        fn = 1;
	elseif n==2
		fn = 2;
	else
		fn = fib(n-1)+fib(n-2);
	end
end