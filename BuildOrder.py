#Build Order 
#projects: a,b,c,d,e,f

def createGraph(projects,dependencies):
    projectGraph={}
    for project in projects:
        projectGraph[project]=[]
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph

project=['a','b','c','d','e','f']
dependencies=[('a','d'),('f','b'),('b','d'),('f','a'),('d','c')]
customGraph=createGraph(project,dependencies)
print(customGraph)

def getProjectsWithDependencies(graph):
    projectsWithDependencies=set()
    for project in graph:
        projectsWithDependencies=projectsWithDependencies.union(set(graph[project]))
    return projectsWithDependencies

projectsWithDependencies=getProjectsWithDependencies(customGraph)
print(projectsWithDependencies)

def getProjectsWODependencies(projectWD,graph):
    projectsWODependencies=set()
    for project in graph:
        if project not in projectWD:
            projectsWODependencies.add(project)
    return projectsWODependencies

print(getProjectsWODependencies(projectsWithDependencies,customGraph))

def findBuildOrder(projects,dependencies):
    buildOrder=[]
    projectGraph=createGraph(projects,dependencies)
    while projectGraph:
        projectsWithDependencies=getProjectsWithDependencies(projectGraph)
        projectsWODependencies=getProjectsWODependencies(projectsWithDependencies,projectGraph)
        if len(projectsWODependencies)==0 and projectGraph:
            raise ValueError("There is a cycle in build order")
        for indProjects in projectsWODependencies:
            buildOrder.append(indProjects)
            del projectGraph[indProjects]
    return buildOrder


print(findBuildOrder(project,dependencies))