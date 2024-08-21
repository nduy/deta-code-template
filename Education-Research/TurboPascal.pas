{

                            Delta Hello Worlfd Code template

}


program Hello;
uses sysutils;

var
   YY,MM,DD : Word;
begin
  writeln ('Hello World!');
     writeln ('Date (as integer) : ',Date);
   DeCodeDate (Date,YY,MM,DD);
   writeln (format ('Today is (DD/MM/YY): %d/%d/%d ',[dd,mm,yy]));
end.
