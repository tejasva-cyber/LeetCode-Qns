class Solution:
    def getImportance(self, employees, id):
        employee_map = {
            employee.id: employee for employee in employees
        }

        def dfs(emp_id):
            employee = employee_map[emp_id]
            total = employee.importance

            for sub_id in employee.subordinates:
                total += dfs(sub_id)

            return total

        return dfs(id)