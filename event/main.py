from website import create_app

if __name__=='__main__':
    app=create_app()
    app.run(debug=True)
    #disable debug mode once successfully deployed