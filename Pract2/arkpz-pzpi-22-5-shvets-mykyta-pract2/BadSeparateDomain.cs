public class Player : GameElement
{
    protected const string player = "O";

    private int prevX;
    private int prevY;

    public Player(int x, int y, GameField field) : base(x, y, field)
    { }

    public override void Draw()
    {
        Console.BackgroundColor = ConsoleColor.DarkGreen;
        Console.ForegroundColor = ConsoleColor.White;
        string emptySpace = new string(' ', player.Length);
        if (prevX != 0 && prevY != 0)
        {
            Console.SetCursorPosition(prevX, prevY);
            Console.Write(emptySpace);
        }
        Console.SetCursorPosition(X, Y);
        Console.Write(player);
        prevX = X;
        prevY = Y;
    }
}