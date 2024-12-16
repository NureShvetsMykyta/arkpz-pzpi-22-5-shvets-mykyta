public class Player : GameElement
{
    protected const string player = "O";

    private int prevX;
    private int prevY;

    public Player(int x, int y, GameField field) : base(x, y, field) { }

    // Домени гравця: збереження попередніх координат
    public int PreviousX => prevX;
    public int PreviousY => prevY;

    public bool PreviousPositionIsValid() => prevX != 0 && prevY != 0;

    public string GetPlayerSymbol() => player;

    public override void Draw() { }
}

public class PlayerRenderer
{
    public void Draw(Player player)
    {
        Console.BackgroundColor = ConsoleColor.DarkGreen;
        Console.ForegroundColor = ConsoleColor.White;

        string emptySpace = new string(' ', player.Length);

        // Очищаємо попередню позицію
        if (player.PreviousPositionIsValid())
        {
            Console.SetCursorPosition(player.PreviousX, player.PreviousY);
            Console.Write(emptySpace);
        }

        // Виводимо нового гравця
        Console.SetCursorPosition(player.X, player.Y);
        Console.Write(player.GetPlayerSymbol());
    }
}
