import  requests
r = requests.post("http://www.ruhsraj.org/results/view_resultsMBBS.php",data={'txtRollNo': '200627', 'txtEnRolYr': '2013', 'txtEnRolNo': '2706', 'result_id': '360','submit': 'View+Results'})
print(r.text)