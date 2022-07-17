/* OO-Lexer for Assignment 1, Comp 311, August 2010 
 * Notes:
 * 1.  This lexer accommodates OO parsing but it is essentially identical the recursive descent lexer.  The ast.java
 *     file contains the OO code including a Token interface with an accept method.
 * 2.  This lexer will be slightly refactored in Assignment 2 to accommodate visitor based dispatch on the operator in
 *     UnOpApp or BinOppApp.
 *
 */
import java.io.*;
import java.util.*;


/** Jam lexer class.              
  * Given a Lexer object, the next token in that input stream being
  * processed by the Lexer is returned by static method readToken(); it
  * throws a ParseException (a form of RuntimeException) if it
  * encounters a syntax error.  Calling readToken() advances the cursor
  * in the input stream to the next token.
  * 
  * The static method peek() in the Lexer class has the same behavior as
  * readToken() except for the fact that it does not advance the cursor.
  */
class Lexer extends StreamTokenizer {
  
  /* short names for StreamTokenizer codes */
  
  public static final int WORD = StreamTokenizer.TT_WORD; 
  public static final int NUMBER = StreamTokenizer.TT_NUMBER; 
  public static final int EOF = StreamTokenizer.TT_EOF; 
  public static final int EOL = StreamTokenizer.TT_EOL; 
  
  /* operator Tokens */
  
  // <unop>  ::= <sign> | ~   | ! 
  // <binop> ::= <sign> | "*" | / | = | != | < | > | <= | >= | & | "|" |
  //             <- 
  // <sign>  ::= "+" | -
  
  //  Note: there is no class distinction between <unop> and <binop> at 
  //  lexical level because of ambiguity; <sign> belongs to both
  
  public static final Op PLUS = new Op("+", true, true); 
  public static final Op MINUS = new Op("-", true, true);
  public static final Op TIMES = new Op("*");
  public static final Op DIVIDE = new Op("/");
  public static final Op EQUALS = new Op("=");
  public static final Op NOT_EQUALS = new Op("!=");
  public static final Op LESS_THAN = new Op("<");
  public static final Op GREATER_THAN = new Op(">");
  public static final Op LESS_THAN_EQUALS = new Op("<=");
  public static final Op GREATER_THAN_EQUALS = new Op(">=");
  public static final Op NOT = new Op("~", true, false);
  public static final Op AND = new Op("&");
  public static final Op OR = new Op("|");
  
  /* Used to support reference cells. */
//  public static final Op BANG = new Op("!", true, false);
//  public static final Op GETS = new Op("<-");
//  public static final Op REF = new Op("ref", true, false);
  
  /* Keywords */

  public static final KeyWord IF     = new KeyWord("if");
  public static final KeyWord THEN   = new KeyWord("then");
  public static final KeyWord ELSE   = new KeyWord("else");
  public static final KeyWord LET    = new KeyWord("let");
//  public static final KeyWord LETREC = new KeyWord("letrec");   // Used to support letrec extension
  public static final KeyWord IN     = new KeyWord("in");
  public static final KeyWord MAP    = new KeyWord("map");
  public static final KeyWord TO     = new KeyWord("to");
  public static final KeyWord BIND   = new KeyWord(":=");
  
  // wordtable for classifying words in token stream
  public HashMap<String,Token>  wordTable = new HashMap<String,Token>();

  // Lexer peek cannot be implemented using StreamTokenizer pushBack 
  // because some Tokens are composed of two StreamTokenizer tokens

  Token buffer;  // holds token for peek() operation
 
  /* constructors */

  /** Constructs a Lexer for the specified inputStream */
  Lexer(Reader inputStream) {
    super(new BufferedReader(inputStream));
    initLexer();
  }

  /** Constructs a Lexer for the contents of the specified file */
  Lexer(String fileName) throws IOException { this(new FileReader(fileName)); }

  /** Constructs a Lexer for the default console input stream System.in */  
  Lexer() {
    super(new BufferedReader(new InputStreamReader(System.in)));
    initLexer();
  }

  /* Initializes lexer tables and the StreamTokenizer that the lexer extends */
  private void initLexer() {

    // configure StreamTokenizer portion of this
    resetSyntax();
    parseNumbers();
    ordinaryChar('-');
    slashSlashComments(true);
    wordChars('0', '9');
    wordChars('a', 'z');
    wordChars('A', 'Z');
    wordChars('_', '_');
    wordChars('?', '?');
    whitespaceChars(0, ' '); 

    // `+' `-' `*' `/' `~' `=' `<' `>' `&' `|' `:' `;' `,' '!'
    // `(' `)' `[' `]' are ordinary characters (self-delimiting)

    initWordTable();
    buffer = null;  // buffer initially empty
  }

  /** Reads tokens until next end-of-line */
  public void flush() throws IOException {
    eolIsSignificant(true);
    while (nextToken() != EOL) ; // eat tokens until EOL
    eolIsSignificant(false);
  }

  /** Returns the next token in the input stream without consuming it */
  public Token peek() { 
    if (buffer == null) buffer = readToken();
    return buffer;
  }
    
  /** Reads the next token as defined by StreamTokenizer in the input stream (consuming it). */
  private int getToken() {
    // synonymous with nextToken() except for throwing an unchecked 
    // ParseException instead of a checked IOException
    try {
      int tokenType = nextToken();
      return tokenType;
    } catch(IOException e) {
      throw new ParseException("IOException " + e + "thrown by nextToken()");
    }
  }

  /** Reads the next Token in the input stream (consuming it) */
  public Token readToken() {
    
    /* Uses getToken() to read next token and  constructs the Token object representing that token.
     * NOTE: token representations for all Token classes except IntConstant are unique; a HashMap 
     * is used to avoid duplication.  Hence, == can safely be used to compare all Tokens except 
     * IntConstants for equality (assuming that code does not gratuitously create Tokens).
     */
    
    if (buffer != null) {
      Token token = buffer;
      buffer = null;          // clear buffer
      return token;
    }
    
    int tokenType = getToken();
    
    switch (tokenType) {
      
      case NUMBER:
        int value = (int) nval;
        if (nval == (double) value) return new IntConstant(value);
        throw new ParseException("The number " + nval + " is not a 32 bit integer");
      case WORD:
        Token regToken = wordTable.get(sval);
        if (regToken == null) {
          // must be new variable name
          Variable newVar = new Variable(sval);
          wordTable.put(sval, newVar);
          return newVar;
        }
        return regToken;
        
      case EOF: return null;
      case '(': return LeftParen.ONLY;
      case ')': return RightParen.ONLY;
      case '[': return LeftBrack.ONLY;
      case ']': return RightBrack.ONLY;
      // case '{': return LeftBrace.ONLY;
      // case '}': return RightBrace.ONLY;
      case ',': return Comma.ONLY;
      case ';': return SemiColon.ONLY;
      
      case '+': return PLUS;  
      case '-': return MINUS;  
      case '*': return TIMES;  
      case '/': return DIVIDE;  
      case '~': return NOT;  
      case '=': return EQUALS;
      
      case '<': 
        tokenType = getToken();
        if (tokenType == '=') return LESS_THAN_EQUALS;  
//      if (tokenType == '-') return GETS;    // Used to support reference cells
        pushBack();
        return LESS_THAN; 
        
      case '>': 
        tokenType = getToken();
        if (tokenType == '=') return GREATER_THAN_EQUALS;  
        pushBack();
        return GREATER_THAN;
        
      case '!': 
        tokenType = getToken();
        if (tokenType == '=') return NOT_EQUALS;  
        else throw new ParseException("!" + ((char) tokenType) + " is not a legal token"); 
        
        /* this  else clause supports reference cells */
//        pushBack();
//        return wordTable.get("!");  
     
      case '&': return AND;  
      case '|': return OR;  
      case ':': {
        tokenType = getToken();
        if (tokenType == '=') return wordTable.get(":=");   // ":=" is a keyword not an operator 
        pushBack();
        throw new ParseException("`:' is not a legalken");
      }
      default:  
        throw new 
        ParseException("`" + ((char) tokenType) + "' is not a legal token");
    }
  }
    
  /** Initializes the table of Strings used to recognize Tokens */
  private void initWordTable() {
    // initialize wordTable

    // constants
    // <null>  ::= null
    // <bool>  ::= true | false

    wordTable.put("null",  NullConstant.ONLY);
    wordTable.put("true",  BoolConstant.TRUE);
    wordTable.put("false", BoolConstant.FALSE);
    
    // Install keywords
    
    wordTable.put("if",   IF);
    wordTable.put("then", THEN);
    wordTable.put("else", ELSE);
    wordTable.put("let",  LET);
    wordTable.put("in",   IN);
    wordTable.put("map",  MAP);
    wordTable.put("to",   TO);
    wordTable.put(":=",   BIND);

    // Install primitive functions
    // <prim>  ::= number? | function? | list? | null? 
    //           | cons? | cons | first | rest | arity

    wordTable.put("number?",   new PrimFun("number?"));
    wordTable.put("function?", new PrimFun("function?"));
//    wordTable.put("ref?",      new PrimFun("ref?"));    // used to support Jam references
    wordTable.put("list?",     new PrimFun("list?"));
    wordTable.put("null?",     new PrimFun("null?"));
    wordTable.put("cons?",     new PrimFun("cons?"));
    wordTable.put("arity",     new PrimFun("arity"));
    wordTable.put("cons",      new PrimFun("cons"));
    wordTable.put("first",     new PrimFun("first"));
    wordTable.put("rest",      new PrimFun("rest"));
  }       

  /** Provides a command line interface to the lexer */
  public static void main(String[] args) throws IOException {
    // check for legal argument list 
    Lexer in;
    if (args.length == 0) {
      in = new Lexer();
    }
    else in = new Lexer(args[0]);
    do {
      Token t = in.readToken();
      if (t == null) break;
      System.out.println("Token " + t + " in " + t.getClass());
    } while (true);
  }
}
