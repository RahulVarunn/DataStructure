CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N =N-1;
  RETURN (

     select Distinct salary from Employee ORDER by salary DESC LIMIT 1 OFFSET N   
  );
END
