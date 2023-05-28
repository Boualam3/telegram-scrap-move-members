# telegram-scrap-move-members
**Disclaimer: This tool is intended for educational and lawful purposes only. I am not responsible for any illegal or unethical use of this tool. Please ensure you comply with all applicable laws and respect the privacy and consent of Telegram users.**



<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>


<!-- GETTING STARTED -->
## Getting Started
This project allows you to scrape members from one Telegram group and add them to own group. It provides a simple and efficient way to automate the process of adding members from one group to another, saving you time and effort.
### Prerequisites
Before you can get started with this project, make sure you have the following prerequisites:

* Python 3.7 or above installed on your machine https://www.python.org/downloads/
* Access to the Telegram API (you will need to create a Telegram Bot and obtain an API token) 
* git https://git-scm.com/
* virtualenv (Recommonded) https://virtualenv.pypa.io/en/latest/


### Installation

1. Get a free API Key at [https://my.telegram.org](https://my.telegram.org)
2. Clone the repo
   ```sh
   git clone https://github.com/Boualam3/telegram-scrap-move-members.git
   ```

3. You can skip this step  I always recommonded use virtualenv on your machine  
   ```sh
      python3 -m venv telegram-scrap-move-members\venv
   ```
   
4. activate virual envirement
   ```sh 
      #unix 
      source venv/bin/activate
      
      #windows cmd
      venv\Scripts\activate.bat
      
   ```
6. Install the required dependencies using pip:
   ```sh
   pip install -r requirements.txt
   ```
4. Enter your API in `get_members.py` and `mv_to_groups.py`
   api_id = your_api_id
   api_hash = your_api_hash
   phone_number = your_number_internationl_format
   



<!-- USAGE EXAMPLES -->
## Usage

1. scrap members using 
  ```sh
     python3 get_members.py 
  ```
  then choose the index of terget groups
2. move the scrapping data `users.csv` to your own group 
  ```sh
     python3 mv_to_group.py
  ```
  then chose the index of distination group

3. Congratulation ( don't addign big number members )






<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>








