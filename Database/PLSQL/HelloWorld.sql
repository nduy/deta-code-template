/* Delta code template */


DECLARE
/*  message varchar2(100):= 'Hello \n World!'; */
  
  message varchar2(100):='hello' || u'\000A' || 'world'|| u'\000A****'|| u'\000A'||'****'|| u'\000A'||'****'|| u'\000A'||'****'|| u'\000A'||'****'|| u'\000A'||'***' || u'\000A'||'**' || u'\000A'||'*';
BEGIN 
  dbms_output.put_line(message); 
END;
/