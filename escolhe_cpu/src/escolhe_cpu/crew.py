from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from escolhe_cpu.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class EscolheCpu():
	"""EscolheCpu crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def cache(self) -> Agent:
		return Agent(
			config=self.agents_config['cache'],
			verbose=True
		)

	@agent
	def tipo_arquitetura(self) -> Agent:
		return Agent(
			config=self.agents_config['tipo_arquitetura'],
			verbose=True
		)

	@agent
	def frequencia(self) -> Agent:
		return Agent(
			config=self.agents_config['frequencia'],
			verbose=True
		)

	@agent
	def escolhe_cpu(self) -> Agent:
		return Agent(
			config=self.agents_config['escolhe_cpu'],
			verbose=True
		)

	@agent
	def justifica_escolha(self) -> Agent:
		return Agent(
			config=self.agents_config['justifica_escolha'],
			verbose=True
		)

	@task
	def cache_task(self) -> Task:
		return Task(
			config=self.tasks_config['cache_task'],
		)

	@task
	def tipo_arquitetura_task(self) -> Task:
		return Task(
			config=self.tasks_config['tipo_arquitetura_task'],
		)

	@task
	def frequencia_task(self) -> Task:
		return Task(
			config=self.tasks_config['frequencia_task'],
		)

	@task
	def escolhe_cpu_task(self) -> Task:
		return Task(
			config=self.tasks_config['escolhe_cpu_task'],
		)

	@task
	def justifica_escolha_task(self) -> Task:
		return Task(
			config=self.tasks_config['justifica_escolha_task'],
			output_file='cpu.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the EscolheCpu crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
