from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType


load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = HuggingFaceHub(
        repo_id="tiiuae/falcon-7b-instruct",
        model_kwargs={"temperature": 0.7,"max_length": 50})
    
    prompt_template_name = PromptTemplate( 
        input_variables=['animal_type','pet_color'],
        template="I have a {animal_type}, and it is {pet_color}. Can you suggest five unique names for it?"
    )
    
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name,
    output_key="pet_name")
    
    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})
    return response

def langchain_agent():
    llm= HuggingFaceHub(
        repo_id="tiiuae/falcon-7b-instruct",
        model_kwargs={"temperature": 0.7})
    
    tools = load_tools(["wikipedia", "llm-math"], llm = llm)
    
    agent = initialize_agent(
        tools = tools, 
        llm = llm, 
        agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True
    )
    result =  agent.run(
        "What is the agerage age of a dog?" 
    )
    
    print(result)
    
if __name__ == "__main__":
    langchain_agent()
    #print(generate_pet_name())
