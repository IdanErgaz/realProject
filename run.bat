rem for chrome

pytest  -v -m "sanity"  --html=\Projects\pythonProject\IdanRealProject\Reports\report.html  --browser chrome

rem pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome

rem pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome

rem pytest -s -v -m "sanity and regression " --html=./Reports/report.html testCases/ --browser chrome

rem pytest -s -v -m "regression" --html=./Reports/report.html testCases/ --browser chrome

rem for firefox

pytest  -v -m "sanity"  --html=\Projects\pythonProject\IdanRealProject\Reports\report.html  --browser firefox

rem pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser firefox

rem pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser firefox

rem pytest -s -v -m "sanity and regression " --html=./Reports/report.html testCases/ --browser firefox

rem pytest -s -v -m "regression" --html=./Reports/report.html testCases/ --browser firefox