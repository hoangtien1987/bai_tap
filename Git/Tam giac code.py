BEGIN
INPUT a,b,c
IF a = 0 or b = 0 or c = 0 THEN
    PRINT "Nhập sai a hoặc b hoặc c"
ELSE
    IF a = b = c THEN
        PRINT "Tam giác đều"
    ELSE
        IF a = b or b = c or c=a THEN
            PRINT "Tam giác cân"
        ELSE
            IF a^2 = b^2 + c^2 or b^2 = a^2 + c^2 or c^2 = a^2 + b^2 THEN
                PRINT "Tam giác vuông"
            ELSE
                PRINT "Tam giác thường"
            END IF
        END IF
    END IF
END IF
END
