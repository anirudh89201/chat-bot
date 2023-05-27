import datetime
import mysql.connector
import openai
if __name__ == "__main__":
    openai.api_key = "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"
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root@123",
        database="mysql"
    )
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS history (
                        QUERY VARCHAR(50) NOT NULL,
                        ANSWER VARCHAR(500) NOT NULL,
                        date DATE NOT NULL
                        );""");
    while (1):
        prompt = input("user: ")

        if (prompt == "exit"):
            break;

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        print("bot: "+response['choices'][0]['message']['content'])
        print()
        res = ""
        res += prompt
        res += "\n"
        res += response['choices'][0]['message']['content']
        date_now = datetime.datetime.now();
        sql = "INSERT INTO CHATGPT (QUERY,ANSWER,date) VALUES (%s, %s, %s)"
        val = (prompt,response['choices'][0]['message']['content'],date_now)
        cursor.execute(sql, val)
        conn.commit()
