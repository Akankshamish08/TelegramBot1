



from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import operator

Token = "7627337934:AAHedf-y5azlMnxDElkfm_aMY-KBAPY6wyU"

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome to Akanmish Bot")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
        /start -> Welcome to the channel 
        /help -> List of all commands
        /content -> About playlist
        /Python -> One Shot video of Python 
        /SQL -> One Shot video of SQL
        /JAVA -> One Shot video of JAVA
        /calc -> If you want to use it as calculator than feel free                          
    """)

async def content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("We have various playlists and articles available")    

async def python(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("tutorial link: https://youtu.be/ERCMXc8x7mc?si=aLYlvH8ioL_9omp3")    

async def sql(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("tutorial link: https://youtu.be/hlGoQC332VM?si=y90nE2zx6zQ7Vr1g")    

async def java(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("tutorial link: https://youtu.be/UmnCZ7-9yDY?si=e7S8v8A_y1dWoF8k")    
async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Join the arguments as a single string
        expression = " ".join(context.args)
        
        # Split expression by space to identify operands and operator
        num1, op, num2 = expression.split()
        num1, num2 = float(num1), float(num2)
        
        # Get the function corresponding to the operator and compute result
        if op in OPERATORS:
            result = OPERATORS[op](num1, num2)
            await update.message.reply_text(f"The result of {num1} {op} {num2} is: {result}")
        else:
            await update.message.reply_text("Unsupported operator. Please use one of +, -, *, /.")
    
    except (ValueError, ZeroDivisionError):
        await update.message.reply_text("Invalid input. Please enter a valid expression like: /calc 3 + 5")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")
# Create the Application instance
app = Application.builder().token(Token).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("content", content))
app.add_handler(CommandHandler("Python", python))
app.add_handler(CommandHandler("SQL", sql))
app.add_handler(CommandHandler("JAVA", java))
app.add_handler(CommandHandler("calc",calc ))
# Start polling
app.run_polling()
