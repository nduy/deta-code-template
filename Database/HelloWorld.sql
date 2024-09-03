-- Delta Code Template
-- create
CREATE TABLE QUOTES (
  empId INTEGER PRIMARY KEY,
  
  name TEXT NOT NULL,
  Favorite_Quote TEXT NOT NULL
);

-- insert
INSERT INTO QUOTES VALUES (0001, 'Clark', '𝐇𝐞𝐥𝐥𝐨 𝐖𝐨𝐫𝐥𝐝!');


-- fetch 

SELECT * FROM QUOTES WHERE name = 'Clark';



DBMS_OUTPUT.PUT_LINE('Area of the rectangle is:')