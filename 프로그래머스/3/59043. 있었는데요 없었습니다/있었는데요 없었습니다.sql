-- 코드를 입력하세요
# SELECT A.ANIMAL_ID, A.NAME
# FROM ANIMAL_INS A
# INNER JOIN ANIMAL_OUTS B ON
#     A.ANIMAL_ID = B.ANIMAL_ID
# WHERE B.DATETIME < A.DATETIME
# ORDER BY A.ANIMAL_ID;

SELECT  AI.ANIMAL_ID
        ,AI.NAME
  FROM  ANIMAL_INS AS AI
 INNER
  JOIN  ANIMAL_OUTS AS AO
    ON  AI.ANIMAL_ID = AO.ANIMAL_ID
 WHERE  AO.DATETIME < AI.DATETIME
 ORDER
    BY  AI.DATETIME
;